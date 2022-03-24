import os
import requests
from multiprocessing.pool import ThreadPool
import numpy as np


def getAccountValue(institutionLinkId: str) -> float:
    url = (
        f"https://www.realizefi.com/api/institution_links/{institutionLinkId}/balances"
    )
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.environ.get('REALIZE_SECRET_KEY')}",
    }
    response = requests.request("GET", url, headers=headers)
    if (response.status_code == 200):
        return float(response.json()["accountValue"])
    print(f"Failed to get balance for institutionLinkId={institutionLinkId}. Found status_code={response.status_code}")
    return 0


if __name__ == "__main__":
    pool = ThreadPool()

    response = requests.get(
        "https://www.realizefi.com/api/users?take=1000",
        headers={"Authorization": f"Bearer {os.environ.get('REALIZE_SECRET_KEY')}"},
    ).json()
    users = response["data"]
    usersWithLinks = list(filter(lambda user: len(user["institutionLinks"]) > 0, users))
    institutionLinks = []
    for user in usersWithLinks:
        institutionLinks += user["institutionLinks"]
    institutionLinkIds = set([link["id"] for link in institutionLinks])
    accountValues = pool.map(getAccountValue, institutionLinkIds)
    print(f"AUM: {sum(accountValues)}")
