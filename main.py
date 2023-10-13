import os
from github import Github

def create_github_labels(repo):
    existing_labels = {label.name: label for label in repo.get_labels()}

    labels_to_add = [
        {"name": "musthave", "color": "FF0000", "description": "リリースに必須なタスクやイシュー"},
        {"name": "medium", "color": "FFA500", "description": "中程度の優先度を持つ項目に使用され、時間とリソースが許す限り取り組むべきタスク"},
        {"name": "dx", "color": "FFA500", "description": "開発者の作業効率やコードの品質に影響を与える"},
        {"name": "ux", "color": "0000FF", "description": "ユーザーの操作性や見た目に影響を与える"},
        {"name": "performance", "color": "800080", "description": "アプリケーションの速度や効率に影響を与える"},
        {"name": "critical", "color": "8B0000", "description": "即時対応が必要な重大な問題"},
        {"name": "minor", "color": "808080", "description": "重要度が低く、時間があるときに対応する問題"}
    ]

    for label in labels_to_add:
        if label["name"] not in existing_labels:
            repo.create_label(name=label["name"], color=label["color"], description=label["description"])
        else:
            print(f"Label {label['name']} already exists.")

if __name__ == "__main__":
    YOUR_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")
    ORG_NAME = os.environ.get("GITHUB_ORG_NAME")

    if YOUR_ACCESS_TOKEN is None or ORG_NAME is None:
        print("Environment variables GITHUB_ACCESS_TOKEN and GITHUB_ORG_NAME must be set.")
        exit(1)

    g = Github(YOUR_ACCESS_TOKEN)
    org = g.get_organization(ORG_NAME)

    for repo in org.get_repos():
        print(f"Adding labels to {repo.name}")
        create_github_labels(repo)

    print("Labels added to all repositories.")
