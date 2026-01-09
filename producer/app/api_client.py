import requests

def fetch_price():
    resp = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={"ids": "bitcoin", "vs_currencies": "usd"}
    )
    resp.raise_for_status()
    return resp.json()
