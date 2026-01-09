import requests
import csv

url = requests.get("https://jsonplaceholder.typicode.com/posts")


def fetch_and_print_posts():
    status = url.status_code
    json_data = url.json()
    if status == 200:
        print(f"Status Code: {status}")
        for data in json_data:
            print(data["title"])
    else:
        print(f"Failed to fetch posts. Status Code: {status}")

def fetch_and_save_posts():
    status = url.status_code
    json_data = url.json()
    data = []
    if status == 200:
        for post in json_data:
            data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=data[0].keys()
            )
            writer.writeheader()
            writer.writerows(data)
