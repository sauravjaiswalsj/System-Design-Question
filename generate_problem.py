import requests
import json
import random
import os
from datetime import datetime

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PROBLEMS = [
    "Design a URL Shortener like Bitly",
    "Design Twitter",
    "Design Netflix",
    "Design Uber",
    "Design WhatsApp",
    "Design Distributed Cache",
    "Design YouTube",
    "Design Instagram"
]

def generate_outline(problem):
    prompt = f"""
You are a senior FAANG system design interviewer.

Generate a structured system design discussion for:

{problem}

Include:

1. Requirements (Functional + Non-functional)
2. High-Level Architecture
3. Database Design
4. Scaling Strategy
5. Bottlenecks
6. Trade-offs

Be concise but technical.
"""
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

    # Check HTTP response
    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")

    data = response.json()

    # Print data for debugging (first run)
    print("API response:", data)

    # Some free AI APIs return 'output_text' or 'result' instead of 'choices'
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    elif "output_text" in data:
        return data["output_text"]
    elif "result" in data:
        return data["result"]
    else:
        raise KeyError(f"Cannot find expected output in API response: {data}")


def main():
    problem = random.choice(PROBLEMS)
    today = datetime.utcnow().strftime("%Y-%m-%d")

    content = generate_outline(problem)

    folder = "interviews/system_design"
    os.makedirs(folder, exist_ok=True)

    filename = f"{today}-{problem.replace(' ', '-').lower()}.md"

    with open(os.path.join(folder, filename), "w") as f:
        f.write(f"# {problem}\n\n")
        f.write(f"Date: {today}\n\n")
        f.write(content)

if __name__ == "__main__":
    main()
