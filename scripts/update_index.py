import os
import json

ARTICLES_DIR = "public/articles"
OUTPUT_FILE = "public/articles.json"

articles = []

for root, _, files in os.walk(ARTICLES_DIR):
    for file in files:
        if file.endswith(".html"):
            full_path = os.path.join(root, file).replace("\\", "/")
            url = full_path.replace("public/", "/")

            articles.append({
                "title": file.replace(".html", "").replace("-", " ").title(),
                "url": url
            })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=2)

print(f"✅ Indexed {len(articles)} articles")
