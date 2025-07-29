
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI()

# Dummy event data
def load_events():
    try:
        df = pd.read_csv("event_data.csv")
        return df.to_dict(orient="records")
    except:
        return []

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    events = load_events()
    table_html = "<table border='1'><tr><th>Názov</th><th>Dátum</th><th>Cena</th><th>Zisk</th><th>AttractiScore</th><th>Odporúčanie</th></tr>"
    for event in events:
        table_html += f"<tr><td>{event.get('name')}</td><td>{event.get('date')}</td><td>{event.get('price')}</td><td>{event.get('profit')}</td><td>{event.get('attract_score')}</td><td>{event.get('recommendation')}</td></tr>"
    table_html += "</table>"
    return HTMLResponse(content=f"<html><head><title>Dashboard</title></head><body><h1>Podujatia</h1>{table_html}</body></html>")
