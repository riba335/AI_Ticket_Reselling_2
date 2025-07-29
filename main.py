from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from scraper import scrape_events

app = FastAPI()

# HTML a CSS sú priamo v hlavnom priečinku
templates = Jinja2Templates(directory=".")

# Dummy fallback - alebo neskôr nahraď scrape_events()
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        df = pd.read_csv("event_data.csv")
        events = df.to_dict(orient="records")
    except Exception:
        events = []
    return templates.TemplateResponse("dashboard.html", {"request": request, "events": events})

@app.get("/health")
def health():
    return {"status": "API is working"}