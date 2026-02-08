import os
import markdown
from pathlib import Path

SRC_DIR = Path("content/articles")
OUT_DIR = Path("public/articles")

OUT_DIR.mkdir(parents=True, exist_ok=True)

for md_file in SRC_DIR.glob("*.md"):
    html_body = markdown.markdown(md_file.read_text(encoding="utf-8"))

    output_file = OUT_DIR / f"{md_file.stem}.html"

    output_file.write_text(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{md_file.stem.replace('-', ' ').title()}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <article>
    {html_body}
  </article>
  <p><a href="../index.html">← Back to home</a></p>
</body>
</html>
""", encoding="utf-8")

print("✅ HTML pages built")
