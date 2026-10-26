import base64
import json
import os
import urllib.request


FORM_ID = "xeaaaewv"
SUBMISSIONS_URL = f"https://formspree.io/api/0/forms/{FORM_ID}/submissions"


def get_submissions():
    credentials = base64.b64encode(f":{os.environ['FORMSPREE_API_KEY']}".encode()).decode()
    request = urllib.request.Request(
        SUBMISSIONS_URL,
        headers={"Authorization": f"Basic {credentials}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(request) as response:
        payload = json.load(response)
    return payload.get("results", [])


def get_field(submission, name):
    content = submission.get("content", {})
    if isinstance(content, dict):
        return content.get(name, "")
    return submission.get(name, "")


def main():
    reviews = []
    for submission in get_submissions():
        if submission.get("spam") is True:
            continue
        try:
            rating = int(get_field(submission, "rating"))
        except (TypeError, ValueError):
            continue
        text = str(get_field(submission, "review")).strip()
        name = str(get_field(submission, "parent_name")).strip()
        if not text or not name or rating not in range(1, 6):
            continue
        reviews.append({"name": name, "rating": rating, "text": text})

    with open("reviews.json", "w", encoding="utf-8") as file:
        json.dump(reviews, file, ensure_ascii=False, indent=2)
        file.write("\n")


if __name__ == "__main__":
    main()
