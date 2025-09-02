import argparse

from github_activity.api import fetch_github_events_by_username
from github_activity.display import render_github_events_table

def main():
    parser = argparse.ArgumentParser(description="GitHub Events CLI")
    parser.add_argument(
        "--username",
        "-u",
        type=str
    )

    args = parser.parse_args()

    username = args.username
    events = fetch_github_events_by_username(username=username)

    print(render_github_events_table(events=events))