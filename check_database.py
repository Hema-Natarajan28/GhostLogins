
from database import initialize_database, save_login, get_all_logins
initialize_database()
event = {
    "username": "demo_user",
    "timestamp": "2026-10-04T03:00:00",
    "success": True,
    "ip_address": "192.0.2.10",
    "location": "Chennai"
}
analysis = {
    "risk_score": 20,
    "risk_level": "MEDIUM",
    "reasons": ["Login during unusual hours"]
}
save_login(event, analysis)
print(get_all_logins())