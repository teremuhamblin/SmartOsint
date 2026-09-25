import requests

def ip_geoloc(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        return r.json()
    except:
        return {"error": "Impossible de géolocaliser l'IP"}
