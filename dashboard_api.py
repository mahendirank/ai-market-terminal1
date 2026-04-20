from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI Market Terminal Running"}

@app.get("/market-data")
def market_data():
    dxy = yf.Ticker("DX-Y.NYB").history(period="1d").Close.iloc[-1]
    gold = yf.Ticker("GC=F").history(period="1d").Close.iloc[-1]
    spx = yf.Ticker("^GSPC").history(period="1d").Close.iloc[-1]

    return {
        "DXY": round(dxy, 2),
        "Gold": round(gold, 2),
        "S&P500": round(spx, 2)
    }

@app.get("/signal")
def signal():
    dxy = yf.Ticker("DX-Y.NYB").history(period="1d").Close.iloc[-1]

    if dxy < 104:
        return {"bias": "GOLD BUY", "reason": "Weak dollar"}
    else:
        return {"bias": "GOLD SELL", "reason": "Strong dollar"}
