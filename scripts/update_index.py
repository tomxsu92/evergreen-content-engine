import os
import json

ARTICLES_DIR = "content/articles"
OUTPUT_FILE = "articles.json"

articles = []

for file in sorted(os.listdir(ARTICLES_DIR), reverse=True):
    if file.endswith(".html"):
        articles.append({
            "title": file.replace(".html", "").replace("-", " "),
            "url": f"{ARTICLES_DIR}/{file}"
        })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=2)

print("articles.json updated")
