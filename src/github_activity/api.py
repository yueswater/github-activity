import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GITHUB_API_KEY")
BASE_URL = "https://api.github.com/users"

HEADERS = {
    "header": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def fetch_github_events_by_username(username: str) -> str:
    url = f"{BASE_URL}/{username}/events"
    print(url)
    response = requests.get(
        url=url,
        headers=HEADERS
    )

    return response.json()

if __name__ == "__main__":
    username = "yueswater"
    events = fetch_github_events_by_username(username=username)
    
    print(events)