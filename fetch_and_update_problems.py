import requests
import json
import os
from datetime import datetime

OUTPUT_FILE = "latest_interview_trends.json"
PROBLEMS_FILE = "problems.json"
INTERVIEW_CATEGORIES = ["system_design", "dsa", "ml_system_design"]
IGNORE_PREFIXES = ["feat:", "fix:", "add:", "merge:", "chore:", "docs:", "refactor:"]

def load_problems():
    if os.path.exists(PROBLEMS_FILE):
        with open(PROBLEMS_FILE, "r") as f:
            return json.load(f)
    else:
        return {cat: [] for cat in INTERVIEW_CATEGORIES}

def save_problems(data):
    with open(PROBLEMS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def fetch_reddit(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}.json?limit=10"
    headers = {"User-Agent": "interview-tracker-bot"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Reddit error: {response.status_code}")
        return []

    data = response.json()
    posts = []

    for post in data["data"]["children"]:
        title = post["data"]["title"].strip()
        link = "https://reddit.com" + post["data"]["permalink"]

        # Include posts mentioning interview, design, or ML
        if (any(k in title.lower() for k in ["interview", "design", "ml", "machine learning", "deep learning"])) \
           and not any(title.lower().startswith(p) for p in IGNORE_PREFIXES):
            posts.append({
                "title": title,
                "source": f"reddit/{subreddit}",
                "url": link
            })

    return posts

def fetch_github_discussions():
    url = "https://api.github.com/search/issues?q=interview+system+design+ml+in:title&sort=updated&order=desc&per_page=10"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"GitHub API error: {response.status_code}")
        return []

    data = response.json()
    results = []

    for item in data.get("items", []):
        title = item["title"].strip()

        # Filter out PR/commit style titles
        if (any(k in title.lower() for k in ["interview", "design", "ml", "machine learning", "deep learning"])) \
           and not any(title.lower().startswith(p) for p in IGNORE_PREFIXES):
            results.append({
                "title": title,
                "source": "github",
                "url": item["html_url"]
            })

    return results

def categorize_title(title):
    lower = title.lower()
    if any(k in lower for k in ["ml", "machine learning", "deep learning"]):
        return "ml_system_design"
    elif "design" in lower:
        return "system_design"
    else:
        return "dsa"

def append_to_problems(trending_posts, problems_data):
    for post in trending_posts:
        title = post["title"].strip()
        category = categorize_title(title)

        # Avoid duplicates
        if title not in problems_data.get(category, []):
            problems_data.setdefault(category, []).append(title)

    return problems_data

def main():
    today = datetime.utcnow().strftime("%Y-%m-%d")

    reddit_leetcode = fetch_reddit("leetcode")
    reddit_systemdesign = fetch_reddit("systemdesign")
    reddit_ml = fetch_reddit("MachineLearning")
    github_results = fetch_github_discussions()

    combined = reddit_leetcode + reddit_systemdesign + reddit_ml + github_results

    # Save trending posts
    with open(OUTPUT_FILE, "w") as f:
        json.dump({"date": today, "results": combined}, f, indent=2)

    print(f"✅ Saved {len(combined)} trending interview discussions to {OUTPUT_FILE}")

    # Load existing problems.json
    problems_data = load_problems()

    # Append new filtered problems
    updated_problems = append_to_problems(combined, problems_data)

    # Save updated problems.json
    save_problems(updated_problems)

    print(f"✅ Updated {PROBLEMS_FILE} with new trending problems.")

if __name__ == "__main__":
    main()
