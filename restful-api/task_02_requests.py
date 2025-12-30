#!/usr/bin/python3
import request


def fetch_and_print_posts():
    """
    fetches all post from JSONPlaceholder
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {:d}".format(response.status_code))
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post.get("title"))

def fetch_and_save_posts():
    """
    fetches all post from JSONPlaceholder
    """
    if response.status_code == 200:
        data = response.json()

        posts_dict = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
                for post in data
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(formatted_posts)
