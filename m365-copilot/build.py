"""Build the Microsoft 365 Copilot package for Flowie's app MCP server.

    python build.py                  # icons + checks + dist/flowie-m365.zip
    python build.py --refresh-tools  # also re-reads tools/list (needs FLOWIE_TOKEN)

Microsoft accepts ASCII only in the manifest and tool file, so the build fails
on any non-ASCII byte. Icons: color 192x192 (full-bleed background), outline
32x32 (white on transparent), per the Teams store icon guidelines.
"""
import json, os, sys, zipfile, pathlib
import resvg_py

HERE = pathlib.Path(__file__).parent
MCP_URL = "https://back.p2p-flowie.com/agent-hub/mcp"
F_PATH = ("M89.7 40.335C78.9 40.335 69.5667 38.535 61.7 34.935L55.3 67.335H93.9C93.9 74.4016 92.1 80.2016 "
          "88.5 84.735C85.0333 89.135 80.1 91.335 73.7 91.335C66.7667 91.335 60.1 90.0683 53.7 87.535C52.3667 "
          "87.0017 51.6333 86.6683 51.5 86.535L40 145.935H0L21.9 14.335H111.1C111.1 22.4683 109.167 28.8683 "
          "105.3 33.535C101.567 38.0683 96.3667 40.335 89.7 40.335Z")


def glyph(x, y, w, h):
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 14.335 111.1 131.6" '
            f'preserveAspectRatio="xMidYMid meet"><path d="{F_PATH}" fill="#FFFFFF"/></svg>')


def icons():
    # Color: full-bleed brand square, glyph inside the 96x96 safe area.
    color = (f'<svg width="192" height="192" viewBox="0 0 192 192" xmlns="http://www.w3.org/2000/svg">'
             f'<rect width="192" height="192" fill="#222878"/>{glyph(48, 48, 96, 96)}</svg>')
    # Outline: white glyph on a transparent background.
    outline = (f'<svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">'
               f'{glyph(4, 4, 24, 24)}</svg>')
    for name, svg in (("color.png", color), ("outline.png", outline)):
        (HERE / name).write_bytes(bytes(resvg_py.svg_to_bytes(svg_string=svg)))


def refresh_tools():
    import requests
    token = os.environ["FLOWIE_TOKEN"]
    r = requests.post(MCP_URL, timeout=120, json={"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}},
                      headers={"Authorization": f"Bearer {token}", "Accept": "application/json, text/event-stream",
                               "User-Agent": "flowie-m365-build/1.0"})
    r.raise_for_status()
    text = r.text
    if "data:" in text[:64]:
        text = [l[5:] for l in text.splitlines() if l.startswith("data:")][-1]
    keep = ("name", "title", "description", "inputSchema", "annotations")
    tools = [{k: v for k, v in t.items() if k in keep} for t in json.loads(text)["result"]["tools"]]
    (HERE / "mcptools.json").write_text(json.dumps({"tools": tools}, ensure_ascii=True, indent=2), encoding="ascii")


def check():
    for name in ("manifest.json", "mcptools.json", "intro.md"):
        raw = (HERE / name).read_bytes()
        bad = [i for i, b in enumerate(raw) if b > 127]
        if bad:
            sys.exit(f"{name}: non-ASCII byte at offset {bad[0]}")
    m = json.loads((HERE / "manifest.json").read_text())
    assert len(m["name"]["short"]) <= 30 and len(m["name"]["full"]) <= 100
    assert len(m["description"]["short"]) <= 80 and len(m["description"]["full"]) <= 4000
    tools = json.loads((HERE / "mcptools.json").read_text())["tools"]
    names = [t["name"] for t in tools]
    assert len(names) == len(set(names)) and all("inputSchema" in t for t in tools)
    return len(tools)


if __name__ == "__main__":
    if "--refresh-tools" in sys.argv:
        refresh_tools()
    icons()
    n = check()
    out = HERE / "dist" / "flowie-m365.zip"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for name in ("manifest.json", "mcptools.json", "intro.md", "color.png", "outline.png"):
            z.write(HERE / name, name)
    print(f"{out} ({n} tools, {out.stat().st_size} bytes)")
