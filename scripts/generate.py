from pathlib import Path
from datetime import datetime
import random
import re

MARKDOWN_DIR = Path("content/articles")
MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)

TOPICS = [
    "How to Organize Your Email Inbox",
    "How to Clean a Coffee Maker",
    "How Often to Replace Air Filters",
    "What Does Bluetooth Do?",
    "What Is Cloud Storage?"
]

def slugify(title):
    return re.sub(r'[^a-z0-9]+', '_', title.lower()).strip('_')

def build_article(title):
    keyword = title.lower()

    return f"""
## What Is {title}?

{title} is a common question people search for when trying to improve efficiency, solve a problem, or understand a tool better. This guide explains it clearly and practically.

---

## Why It Matters

Understanding {keyword} helps you:

- Save time
- Avoid common mistakes
- Improve long-term efficiency
- Make smarter decisions

---

## Step-by-Step Guide to {title}

### Step 1: Understand the Basics
Start by identifying the main goal and common problems related to this topic.

### Step 2: Apply Best Practices
Follow proven methods used by professionals to get consistent results.

### Step 3: Maintain and Optimize
Regularly review and improve your process to maximize results.

---

## Common Mistakes to Avoid

- Ignoring maintenance
- Overcomplicating the process
- Not reviewing performance regularly

---

## Final Thoughts

By understanding and applying these principles of {keyword}, you can improve outcomes and avoid unnecessary frustration.
"""

def generate_article():
    today = datetime.now().strftime("%Y-%m-%d")
    title = random.choice(TOPICS)
    slug = slugify(title)

    # make filename unique per day
    filename = f"{today}_{slug}.md"
    markdown_path = MARKDOWN_DIR / filename

    article_body = build_article(title)

    markdown_content = f"""---
title: {title}
date: {today}
description: Educational guide about {title.lower()}.
---

# {title}

{article_body}
"""

    markdown_path.write_text(markdown_content, encoding="utf-8")

    print(f"✅ Article generated: {filename}")

if __name__ == "__main__":
    generate_article()<li>Improve long-term efficiency</li>
<li>Make smarter decisions</li>
</ul>

<hr>

<h2>Step-by-Step Guide to {title}</h2>

<h3>Step 1: Understand the Basics</h3>
<p>Start by identifying the main goal and common problems related to this topic.</p>

<h3>Step 2: Apply Best Practices</h3>
<p>Follow proven methods used by professionals to get consistent results.</p>

<h3>Step 3: Maintain and Optimize</h3>
<p>Regularly review and improve your process to maximize results.</p>

<hr>

<h2>Common Mistakes to Avoid</h2>
<ul>
<li>Ignoring maintenance</li>
<li>Overcomplicating the process</li>
<li>Not reviewing performance regularly</li>
</ul>

<hr>

<h2>Final Thoughts</h2>
<p>By understanding and applying these principles of {keyword}, you can improve outcomes and avoid unnecessary frustration.</p>
"""

def generate_article():
    today = datetime.now().strftime("%Y-%m-%d")
    title = random.choice(TOPICS)
    slug = slugify(title)

    markdown_filename = MARKDOWN_DIR / f"{slug}.md"
    html_filename = HTML_DIR / f"{slug}.html"

    if markdown_filename.exists():
        print("⚠ Article already exists")
        return

    # Build HTML body
    article_body = build_article(title)

    # Write Markdown (for archive / future use)
    markdown_content = f"""---
title: {title}
date: {today}
description: Educational guide about {title.lower()}.
---

# {title}

{article_body}
"""
    markdown_filename.write_text(markdown_content, encoding="utf-8")

    # Write full HTML page
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>

<div class="container">

<h1>{title}</h1>
<p><em>Published on {today}</em></p>

{article_body}

<p><a href="/">← Back to home</a></p>

</div>

</body>
</html>
"""
    html_filename.write_text(html_content, encoding="utf-8")

    print(f"✅ Article generated: {slug}.html")

if __name__ == "__main__":
    generate_article()
