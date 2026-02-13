import requests
import json
import random
import os
from datetime import datetime

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PROBLEMS_FILE = "problems.json"
INTERVIEWS_DIR = "interviews"

def load_problems():
    """Load all problem titles from problems.json."""
    if not os.path.exists(PROBLEMS_FILE):
        raise FileNotFoundError(f"{PROBLEMS_FILE} not found")

    with open(PROBLEMS_FILE, "r") as f:
        data = json.load(f)

    # Flatten all categories into a single list of (category, problem) tuples
    all_problems = []
    for category, problems in data.items():
        for problem in problems:
            all_problems.append((category, problem))
    return all_problems

def generate_outline(problem):
    prompt = f"""
You are a principal FAANG system design interviewer.

Generate a structured system design discussion for:

{problem}

Include:

1. Requirements (Functional + Non-functional)
2. High-Level Architecture
3. Database Design
4. Scaling Strategy
5. Bottlenecks
6. Trade-offs

Be concise and technical. Follow proper system design principles and include relevant learning links if possible.

Also, explain the {problem} solution using the first principle of system design.
"""
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set! Add it as a GitHub secret.")

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
    )

    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")

    data = response.json()
    # Print data for debugging (first run) 
    #print("API response:", data)
    
    # Adjust to your API response keys
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    elif "output_text" in data:
        return data["output_text"]
    elif "result" in data:
        return data["result"]
    else:
        raise KeyError(f"Cannot find expected output in API response: {data}")


def main():
    all_problems = load_problems()
    if not all_problems:
        print("No problems found in JSON!")
        return

    # Pick a random problem from JSON
    category, problem = random.choice(all_problems)
    today = datetime.utcnow().strftime("%Y-%m-%d")

    content = generate_outline(problem)

    folder = os.path.join(INTERVIEWS_DIR, category)
    os.makedirs(folder, exist_ok=True)

    # Create a safe filename
    filename = f"{today}-{problem.replace(' ', '-').lower()}.md"

    with open(os.path.join(folder, filename), "w") as f:
        f.write(f"# {problem}\n\n")
        f.write(f"Category: {category}\n")
        f.write(f"Date: {today}\n\n")
        f.write(content)

    print(f"✅ Generated {filename} in {folder}")


if __name__ == "__main__":
    main()
