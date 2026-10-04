from detector import analyze_login
event = {
    "username": "demo_user",
    "timestamp": "2026-10-04T03:00:00",
    "success": True,
    "ip_address": "192.0.2.10",
    "location": "Chennai"
}
result = analyze_login(event, [])
print(result)