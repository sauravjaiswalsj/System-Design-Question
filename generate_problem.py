import json
import random
import os
from datetime import datetime
import re

BASE_DIR = "interviews"

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def load_problems():
    with open("problems.json") as f:
        return json.load(f)

def generate_markdown(problem, category):
    today = datetime.utcnow().strftime("%Y-%m-%d")

    return f"""# {problem}

**Category:** {category}  
**Date:** {today}

---

## 1. Requirements Clarification

- Functional requirements:
- Non-functional requirements:
- Constraints:

---

## 2. High-Level Design

- Core components:
- APIs:
- Data flow:

---

## 3. Deep Dive

- Database design:
- Scaling strategy:
- Caching:
- Trade-offs:

---

## 4. Bottlenecks & Improvements

- 

---

## 5. Follow-up Questions

- 
"""

def main():
    problems = load_problems()
    category = random.choice(list(problems.keys()))
    problem = random.choice(problems[category])

    today = datetime.utcnow().strftime("%Y-%m-%d")
    slug = slugify(problem)

    folder = os.path.join(BASE_DIR, category)
    os.makedirs(folder, exist_ok=True)

    filename = f"{today}-{slug}.md"
    filepath = os.path.join(folder, filename)

    if not os.path.exists(filepath):
        content = generate_markdown(problem, category)
        with open(filepath, "w") as f:
            f.write(content)

if __name__ == "__main__":
    main()
