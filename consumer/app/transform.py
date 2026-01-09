def transform_price(event):
    return {
        "asset": "BTC",
        "price": event["bitcoin"]["usd"]
    }
