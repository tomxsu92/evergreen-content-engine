from pathlib import Path
from datetime import datetime
import random
import re

MARKDOWN_DIR = Path("content/articles")
MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)

BASE_TOPICS = [
    "Productivity",
    "Home Maintenance",
    "Technology Basics",
    "Personal Finance",
    "Digital Organization",
    "Time Management",
    "Computer Skills",
    "Household Cleaning",
    "Internet Safety",
    "Smart Devices"
]

TEMPLATES = [
    "Beginner Guide to {}",
    "How {} Works",
    "Understanding {} Made Simple",
    "Step-by-Step {} Guide",
    "Complete Introduction to {}"
]

def slugify(title):
    return re.sub(r'[^a-z0-9]+', '_', title.lower()).strip('_')

def build_article(title):
    keyword = title.lower()

    return f"""
## Introduction

{title} is an important topic that many people want to understand better. This guide provides a clear and practical explanation.

---

## Why It Matters

Understanding {keyword} can help improve efficiency, reduce mistakes, and build confidence.

---

## Core Concepts

### 1. Foundation
Start by learning the basic principles behind {keyword}.

### 2. Practical Application
Apply these ideas consistently to see real improvement.

### 3. Optimization
Review and refine your approach regularly.

---

## Common Mistakes

- Skipping fundamentals
- Overcomplicating processes
- Ignoring consistency

---

## Final Thoughts

With a structured approach to {keyword}, you can build long-term knowledge and better results.
"""

def generate_article():
    today = datetime.now().strftime("%Y-%m-%d")

    topic = random.choice(BASE_TOPICS)
    template = random.choice(TEMPLATES)

    title = template.format(topic)
    slug = slugify(f"{today}_{title}")

    markdown_path = MARKDOWN_DIR / f"{slug}.md"

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

    print(f"Article generated: {slug}.md")

if __name__ == "__main__":
    generate_article()
