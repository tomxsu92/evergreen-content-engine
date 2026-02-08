import os
import json
from pathlib import Path

# ===== CONFIG =====
REPO_NAME = "evergreen-content-engine"
ARTICLES_DIR = "content/articles"
OUTPUT_FILE = "public/articles.json"

articles = []

# Make sure output directory exists
os.makedirs("public", exist_ok=True)

for md_file in Path(ARTICLES_DIR).glob("*.md"):
    title = md_file.stem.replace("_", " ").replace("-", " ").title()

    # GitHub Pages project-site safe URL
    url = f"/{REPO_NAME}/{ARTICLES_DIR}/{md_file.name}"

    articles.append({
        "title": title,
        "url": url
    })

# Write articles.json
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=2)

print(f"✅ Indexed {len(articles)} articles into {OUTPUT_FILE}")
