from datetime import datetime, time
def analyze_login(event, recent_events):
    score = 0
    reasons = []
    username = event["username"]
    event_time = datetime.fromisoformat(event["timestamp"])
    failed_count = sum(
        1 for previous in recent_events
        if previous["username"] == username
        and not previous["success"]
        and 0 <= (
            event_time - datetime.fromisoformat(
                previous["timestamp"]
            )
        ).total_seconds() <= 600
    )
    if not event["success"]:
        failed_count += 1
    if failed_count >= 5:
        score += 50
        reasons.append("Repeated failed login attempts")
    login_time = event_time.time()
    if time(0, 0) <= login_time < time(5, 0):
        score += 20
        reasons.append("Login during unusual hours")
    known_locations = {
        previous["location"]
        for previous in recent_events
        if previous["username"] == username
        and previous["success"]
    }
    if (
        event["success"]
        and known_locations
        and event["location"] not in known_locations
    ):
        score += 30
        reasons.append("Unfamiliar login location")
    score = min(score, 100)
    if score >= 50:
        risk_level = "HIGH"
    elif score >= 20:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    return {
        "risk_score": score,
        "risk_level": risk_level,
        "reasons": reasons,
    }