import os
from dotenv import load_dotenv
import requests
import json
import schedule
from discord import send_embedded_message

load_dotenv()

# Notion API token and database ID
TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

# Headers for API requests
HEADERS = {
    "Authorization": "Bearer " + TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13",
}

# File to store a copy of the database
DB_FILE = "./db.json"

# Read the database with the given ID and headers
def read_database(database_id, headers):
    read_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    res = requests.request("POST", read_url, headers=headers)
    data = res.json()
    return data


# Extract certain properties from the database
def get_data(data):
    ids = []

    # Extract data for each task in the database
    tasks = [i for i in data["results"]]
    sample_db = {}
    for task in tasks:
        sample_db[task["id"]] = {
            "status": task["properties"]["Статус"]["status"]["name"],
            "url": task["url"],
            "title": task["properties"]["Task name"]["title"][0]["plain_text"],
            "users": [user["name"] for user in task["properties"]["Исполнитель"]["people"]],
            "tags": [tag["name"] for tag in task["properties"]["Теги"]["multi_select"]],
            "task_id": task["properties"]["Task ID"]["unique_id"]["number"],
        }

    return sample_db


# Compare two copies of the database and check if the status of any tasks has changed
def check_db(data1, data2):
    for task_id in data1.keys():
        if task_id in data2.keys():
            # Check if the status of the task has changed
            if data1[task_id] == data2[task_id]:
                pass
            else:
                field = [
                    {"name": "Task id", "value": data2[task_id]["task_id"]},
                    {"name": "Status", "value": data2[task_id]["status"]},
                    {"name": "Users", "value": ",".join(data2[task_id]["users"])},
                    {"name": "Tags", "value": ",".join(data2[task_id]["tags"])},
                ]

                send_embedded_message(
                    "[" + data2[task_id]["status"] + "] " + data2[task_id]["title"] + "(" + ",".join(data2[task_id]["tags"]) + ")",
                    data2[task_id]["url"],
                    fields=field,
                    data=data2[task_id]
                )
        # Task not found in second copy of database
        else:
            print("Not found")


# Main function to check if the database has changed
def main():
    # Read the current version of the database
    current_db = get_data(read_database(DATABASE_ID, HEADERS))
    # Read the previous version of db
    old_db = json.load(open(DB_FILE, "r", encoding="utf8"))
    # Check if the database has changed
    check_db(old_db, current_db)
    # Update the database file
    with open(DB_FILE, "w", encoding="utf8") as f:
        json.dump(current_db, f, ensure_ascii=False, indent=4)

    return


if __name__ == "__main__":
    main()
#     # Run the main function every 15 seconds
#     schedule.every(5).minutes.do(main)
#
#     while True:
#         schedule.run_pending()