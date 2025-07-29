from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dummy data - sem sa neskôr doplní API call
events = [
    {"name": "The Weeknd - Bratislava", "date": "2025-08-10", "price": "89€"},
    {"name": "Coldplay - Vienna", "date": "2025-08-22", "price": "120€"},
    {"name": "Imagine Dragons - Prague", "date": "2025-09-05", "price": "99€"},
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "events": events})

@app.get("/health")
def health():
    return {"status": "API is working"}
