import os
import requests
from multiprocessing.pool import ThreadPool
from typing import TypedDict
import numpy as np


class Position(TypedDict):
    marketValue: str


def getAccountValue(institutionLinkId: str) -> float:
    url = (
        f"https://www.realizefi.com/api/institution_links/{institutionLinkId}/balances"
    )
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.environ.get('REALIZE_SECRET_KEY')}",
    }
    return float(requests.request("GET", url, headers=headers).json()["accountValue"])


if __name__ == "__main__":
    pool = ThreadPool()

    response = requests.get(
        "https://www.realizefi.com/api/users",
        headers={"Authorization": f"Bearer {os.environ.get('REALIZE_SECRET_KEY')}"},
    ).json()
    users = response["data"]
    usersWithLinks = list(filter(lambda user: len(user["institutionLinks"]) > 0, users))

    userLinks = [user["institutionLinks"] for user in usersWithLinks]
    institutionLinks = list(np.array(userLinks).reshape(-1))
    institutionLinkIds = [link["id"] for link in institutionLinks]
    accountValues = pool.map(getAccountValue, institutionLinkIds)
    print(f"AUM: {sum(accountValues)}")