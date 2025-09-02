from tabulate import tabulate
from typing import List, Dict

def render_github_events_table(events: List[Dict]) -> str:
    table_data = []

    headers = ["ID", "Created At", "Type", "Repository Name", "Commit Message"]

    for event in events:
        commit = event["payload"].get("commits", [{}])[0]
        message = commit["message"][:50] if commit else ""

        table_data.append([
            event["id"],
            event["created_at"],
            event["type"],
            event["repo"]["name"],
            message
            # event["payload"]["commits"][0]["message"][:50] if len(event["commits"][0]["message"]) > 50 else event["commits"][0]["message"]
        ])

    return tabulate(
        tabular_data=table_data,
        headers=headers,
        tablefmt="fancy_grid"
    )