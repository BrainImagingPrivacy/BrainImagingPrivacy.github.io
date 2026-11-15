"""Build the audience pages and glossary: python scripts/build_site.py."""
from pathlib import Path
import shutil
import tomllib
import markdown
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markupsafe import Markup

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs"
OUTPUT = ROOT / "_site"
REPO = "https://github.com/BrainImagingPrivacy/BrainImagingPrivacy.github.io"
PAGES = ["index", "researchers", "participants", "legal", "policy", "glossary"]

def build():
    env = Environment(loader=FileSystemLoader(SOURCE / "_layouts"),
                      autoescape=True, undefined=StrictUndefined)
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    shutil.copytree(SOURCE / "assets", OUTPUT / "assets")
    for slug in PAGES:
        source = SOURCE / f"{slug}.md"
        raw = source.read_text(encoding="utf-8")
        if not raw.startswith("+++\n"):
            raise ValueError(f"Missing TOML metadata in {source}")
        _, header, body = raw.split("+++", 2)
        page = tomllib.loads(header)
        md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list"],
                               extension_configs={"toc": {"toc_depth": "2"}})
        html = md.convert(body).replace('<table>', '<div class="table-scroll" role="region" aria-label="Comparison table" tabindex="0"><table>').replace('</table>', '</table></div>')
        content = Markup(html)
        rendered = env.get_template("home.html" if slug == "index" else "audience.html").render(
            page=page, slug=slug, content=content, toc=Markup(md.toc), repo=REPO,
            edit_url=f"{REPO}/edit/main/docs/{slug}.md")
        (OUTPUT / f"{slug}.html").write_text(rendered, encoding="utf-8")
    (OUTPUT / ".nojekyll").touch()
    print(f"Built {len(PAGES)} pages in {OUTPUT}")

if __name__ == "__main__":
    build()
