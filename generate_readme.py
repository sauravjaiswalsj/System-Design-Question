import os

INTERVIEW_DIR = "interviews"
README_FILE = "README.md"

def get_all_problems():
    problems_list = []
    # Walk through interviews/system_design and interviews/dsa
    for category in os.listdir(INTERVIEW_DIR):
        category_path = os.path.join(INTERVIEW_DIR, category)
        if os.path.isdir(category_path):
            for filename in sorted(os.listdir(category_path)):
                if filename.endswith(".md"):
                    file_path = os.path.join(category_path, filename)
                    display_name = filename.replace(".md", "").replace("-", " ").title()
                    problems_list.append((category, display_name, file_path))
    return problems_list

def generate_readme(problems):
    lines = [
        "# Interview Preparation Repository",
        "",
        "This repository contains curated FAANG-level interview problems (System Design + DSA).",
        "",
    ]

    categories = sorted(set([p[0] for p in problems]))
    for category in categories:
        lines.append(f"## {category.replace('_', ' ').title()}")
        lines.append("")
        for cat, display_name, file_path in problems:
            if cat == category:
                lines.append(f"- [{display_name}]({file_path})")
        lines.append("")

    return "\n".join(lines)

def main():
    problems = get_all_problems()
    readme_content = generate_readme(problems)

    with open(README_FILE, "w") as f:
        f.write(readme_content)
    print(f"✅ Updated {README_FILE} with {len(problems)} problems.")

if __name__ == "__main__":
    main()
