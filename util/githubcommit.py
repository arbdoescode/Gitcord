import requests
import json

def fetch_commits(repo_owner, repo_name):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch commitsss: {response.status_code}")
        return []

def format_commits(commit_data):
    formatted = []
    for item in commit_data:
        commit_info = {
            "author": item["commit"]["author"]["name"],
            "time": item["commit"]["author"]["date"],
            "sha": item["sha"],
            "message": item["commit"]["message"].split("\n")[0]
        }
        formatted.append(commit_info)
    return formatted