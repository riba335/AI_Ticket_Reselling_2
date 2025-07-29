def analyze_event(event):
    score = calculate_attractiveness(event)
    recommended = score > 75 and (event.ticket_price * event.capacity * 0.6) - event.marketing_spend > 30
    return {
        "AttractiScore": score,
        "recommended": recommended
    }

def calculate_attractiveness(event):
    score = (
        event.artist_popularity * 0.4 +
        (100 - event.ticket_price) * 0.2 +
        (event.capacity / 1000) * 0.2 +
        (event.marketing_spend / 1000) * 0.2
    )
    return round(score, 2)
