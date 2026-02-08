import os
import markdown
from pathlib import Path

ARTICLES_DIR = "content/articles"
OUTPUT_DIR = "public/articles"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for md_file in Path(ARTICLES_DIR).glob("*.md"):
    with open(md_file, "r", encoding="utf-8") as f:
        html = markdown.markdown(f.read())

    output_file = Path(OUTPUT_DIR) / (md_file.stem + ".html")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{md_file.stem.replace("_", " ").title()}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <article>
    {html}
  </article>
</body>
</html>
""")

print("HTML build complete")
