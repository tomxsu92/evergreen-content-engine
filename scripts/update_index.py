import json
from pathlib import Path

REPO_NAME = "evergreen-content-engine"
ARTICLES_DIR = Path("public/articles")
OUTPUT_FILE = Path("public/articles.json")

articles = []

for html_file in ARTICLES_DIR.glob("*.html"):
    articles.append({
        "title": html_file.stem.replace("-", " ").title(),
        "url": f"/{REPO_NAME}/articles/{html_file.name}"
    })

OUTPUT_FILE.write_text(json.dumps(articles, indent=2), encoding="utf-8")

print(f"✅ Indexed {len(articles)} articles")
