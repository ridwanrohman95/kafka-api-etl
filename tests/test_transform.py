from consumer.app.transform import transform_price

def test_transform_price():
    event = {"bitcoin": {"usd": 50000}}
    result = transform_price(event)

    assert result["asset"] == "BTC"
    assert result["price"] == 50000
