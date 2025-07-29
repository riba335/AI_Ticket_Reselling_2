import csv
from datetime import datetime

def scrape_events():
    events = [
        {"name": "The Weeknd - Bratislava", "date": "2025-08-10", "price": "89€"},
        {"name": "Coldplay - Vienna", "date": "2025-08-22", "price": "120€"},
        {"name": "Imagine Dragons - Prague", "date": "2025-09-05", "price": "99€"}
    ]
    with open("event_data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "date", "price"])
        writer.writeheader()
        writer.writerows(events)

if __name__ == "__main__":
    scrape_events()