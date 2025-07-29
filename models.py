from pydantic import BaseModel

class EventInput(BaseModel):
    name: str
    location: str
    date: str
    artist_popularity: float
    ticket_price: float
    capacity: int
    marketing_spend: float
