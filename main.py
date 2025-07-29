from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

# Dummy data – môžeš neskôr nahradiť reálnymi API dátami
events = [
    {"name": "The Weeknd - Bratislava", "date": "2025-08-10", "price": "89€"},
    {"name": "Coldplay - Vienna", "date": "2025-08-22", "price": "120€"},
    {"name": "Imagine Dragons - Prague", "date": "2025-09-05", "price": "99€"},
]

# Hlavná stránka s tabuľkou
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Načíta HTML súbor a vloží do neho eventy
    with open("dashboard.html", encoding="utf-8") as f:
        html = f.read()

    # Vygenerovanie riadkov tabuľky
    rows = ""
    for event in events:
        rows += f"<tr><td>{event['name']}</td><td>{event['date']}</td><td>{event['price']}</td></tr>"

    # Nahradí placeholder v HTML šablóne
    html = html.replace("{{event_rows}}", rows)
    return HTMLResponse(content=html)

# Endpoint pre CSS (štýly)
@app.get("/style.css")
def get_css():
    return FileResponse("style.css")

# Testovací endpoint
@app.get("/health")
def health():
    return {"status": "API is working"}