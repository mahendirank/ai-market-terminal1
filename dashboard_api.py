from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Market Terminal Running"}

@app.get("/signal")
def get_signal():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        data = requests.get(url).json()

        eur = data["rates"]["EUR"]

        if eur > 0.9:
            return {
                "bias": "GOLD BUY",
                "reason": "USD weak"
            }
        else:
            return {
                "bias": "GOLD SELL",
                "reason": "USD strong"
            }

    except:
        return {
            "bias": "NO TRADE",
            "reason": "Error fetching data"
        }
