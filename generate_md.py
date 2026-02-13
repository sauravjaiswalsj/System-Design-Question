import json
import os

PROBLEMS_FILE = "problems.json"
DOCS_DIR = "docs"

os.makedirs(DOCS_DIR, exist_ok=True)

with open(PROBLEMS_FILE) as f:
    data = json.load(f)

# Home page
with open(os.path.join(DOCS_DIR, "index.md"), "w") as f:
    f.write("# Interview Problem Hub\n\n")
    f.write("This repository contains daily curated interview problems in DSA, System Design, and ML System Design.\n\n")

# Category pages
for category, problems in data.items():
    filename = os.path.join(DOCS_DIR, f"{category}.md")
    with open(filename, "w") as f:
        f.write(f"# {category.replace('_',' ').title()}\n\n")
        for i, problem in enumerate(problems, start=1):
            f.write(f"{i}. {problem}\n")
