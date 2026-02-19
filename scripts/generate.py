from pathlib import Path
from datetime import datetime
import random
import re

ARTICLES_DIR = Path("content/articles")
ARTICLES_DIR.mkdir(parents=True, exist_ok=True)

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

    return f"""# {title}

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

# Pick one topic per day
today = datetime.now().strftime("%Y%m%d")
title = random.choice(TOPICS)
slug = slugify(title)
filename = f"{slug}.md"

file_path = ARTICLES_DIR / filename

if not file_path.exists():
    content = build_article(title)
    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Article generated: {filename}")
else:
    print("⚠ Article already exists")
