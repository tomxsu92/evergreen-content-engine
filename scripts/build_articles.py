import os
import json
import markdown

ARTICLES_MD = "content/articles"
ARTICLES_HTML = "articles"
INDEX_FILE = "articles.json"

os.makedirs(ARTICLES_HTML, exist_ok=True)

articles_index = []

for filename in os.listdir(ARTICLES_MD):
    if not filename.endswith(".md"):
        continue

    slug = filename.replace(".md", "")
    md_path = os.path.join(ARTICLES_MD, filename)
    html_path = os.path.join(ARTICLES_HTML, f"{slug}.html")

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content)

    html_page = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{slug.replace('-', ' ').title()}</title>
</head>
<body>
  <a href="/">← Back</a>
  {html_body}
</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_page)

    articles_index.append({
        "title": slug.replace("-", " ").title(),
        "slug": slug,
        "path": f"articles/{slug}.html"
    })

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    json.dump(articles_index, f, indent=2)
