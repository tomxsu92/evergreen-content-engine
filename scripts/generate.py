from pathlib import Path
from datetime import datetime

ARTICLES_DIR = Path("content/articles")
ARTICLES_DIR.mkdir(parents=True, exist_ok=True)

filename = f"example-{datetime.now().strftime('%Y%m%d')}.md"
file_path = ARTICLES_DIR / filename

if not file_path.exists():
    file_path.write_text(
        "# Example Article\n\n"
        "This is an automatically generated article.\n",
        encoding="utf-8"
    )

print("✅ Article generated")
