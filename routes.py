from fastapi import APIRouter
from models import EventInput
from logic import analyze_event

router = APIRouter()

@router.post("/analyze_event")
def analyze(event: EventInput):
    return analyze_event(event)
