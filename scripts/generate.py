import datetime

TOPICS = [
    "How to clean a coffee maker",
    "What is cloud storage",
    "How often to replace air filters",
    "What does Bluetooth do",
    "How to organize email inbox"
]

def generate_article(topic):
    today = datetime.date.today()
    return f"""---
title: {topic}
date: {today}
description: Educational guide about {topic.lower()}.
---

## {topic}

This article provides general informational content only.

### Overview
This article explains {topic.lower()} in simple terms.

### Disclaimer
This content is for informational purposes only.
"""

def main():
    topic = TOPICS[datetime.date.today().day % len(TOPICS)]
    filename = f"content/articles/{topic.replace(' ', '_').lower()}.md"
    with open(filename, "w") as f:
        f.write(generate_article(topic))

if __name__ == "__main__":
    main()
