import os
import json

ARTICLES_DIR = "content/articles"
OUTPUT_FILE = "articles.json"

articles = []

for root, _, files in os.walk(ARTICLES_DIR):
    for file in files:
        if file.endswith(".html"):
            full_path = os.path.join(root, file).replace("\\", "/")
            articles.append({
                "title": file.replace(".html", "").replace("-", " ").title(),
                "url": full_path
            })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=2)

print(f"✅ Indexed {len(articles)} articles")
