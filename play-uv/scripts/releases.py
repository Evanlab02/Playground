# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests==2.32.3",
# ]
# ///

import sys
from datetime import datetime, timedelta
from json import dump
import requests


def main() -> int:
    """Entry point for the releases script."""
    timestamp = datetime.now()
    try:
        with open("src/data/timestamp.txt", "r", encoding="UTF-8") as timestamp_data:
            old_timestamp = timestamp_data.readlines()[0]
            old_timestamp = datetime.fromisoformat(old_timestamp)
            if old_timestamp + timedelta(days=1) > timestamp:
                print("Data is still valid...")
                return 0
    except Exception:
        print("No cache found...")
        print("Refreshing...")

    session = requests.Session()
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = session.get(
        "https://api.github.com/repos/psf/requests/releases", headers=headers
    )
    with open("src/data/data.json", "w+", encoding="UTF-8") as data:
        dump(response.json(), data, indent=4)

    with open("src/data/timestamp.txt", "w+", encoding="UTF-8") as timestamp_data:
        timestamp_data.write(timestamp.isoformat())
    return 0


if __name__ == "__main__":
    EXIT = main()
    print("Done")
    sys.exit(EXIT)
