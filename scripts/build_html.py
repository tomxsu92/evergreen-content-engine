from pathlib import Path
import markdown
import json
import re

CONTENT_DIR = Path("content/articles")
OUTPUT_DIR = Path("articles")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

articles_data = []

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '_', text.lower()).strip('_')

for md_file in CONTENT_DIR.glob("*.md"):
    content = md_file.read_text(encoding="utf-8")

    parts = content.split("---")
    if len(parts) < 3:
        continue

    front_matter = parts[1]
    body = parts[2]

    title = ""
    date = ""
    description = ""

    for line in front_matter.splitlines():
        if line.startswith("title:"):
            title = line.replace("title:", "").strip()
        if line.startswith("date:"):
            date = line.replace("date:", "").strip()
        if line.startswith("description:"):
            description = line.replace("description:", "").strip()

    slug = slugify(title)
    html_body = markdown.markdown(body)

    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>

<div class="container">

<h1>{title}</h1>
<p><em>Published on {date}</em></p>

{html_body}

<p><a href="../index.html">← Back to home</a></p>

</div>

</body>
</html>
"""

    html_path = OUTPUT_DIR / f"{slug}.html"
    html_path.write_text(html_content, encoding="utf-8")

    articles_data.append({
        "title": title,
        "date": date,
        "description": description,
        "slug": slug
    })

with open("articles.json", "w", encoding="utf-8") as f:
    json.dump(articles_data, f, indent=2)

print("✅ HTML pages rebuilt successfully.")
