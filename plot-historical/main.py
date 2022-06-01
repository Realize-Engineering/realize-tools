import matplotlib.pyplot as plt
import requests
import os
from dotenv import load_dotenv

load_dotenv()

REALIZE_SECRET_KEY = os.environ.get("REALIZE_SECRET_KEY")
REALIZE_INSTITUTION_LINK_ID = os.environ.get("REALIZE_INSTITUTION_LINK_ID")
REALIZE_API_URL = os.environ.get("REALIZE_API_URL")

if __name__ == "__main__":
    print("Begin plotting")
    response = requests.get(
        f"{REALIZE_API_URL}/institution_links/{REALIZE_INSTITUTION_LINK_ID}/historical_performance?span=day",
        headers={"Authorization": f"Bearer {REALIZE_SECRET_KEY}"},
    )
    data = response.json()["data"]
    print(f"Received json with interval {data['interval']}")
    plt.plot([round(float(y), 5) for y in data["equity"]])
    plt.show()
