import requests

def email_lookup(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": "YOUR_API_KEY"}

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return {"email": email, "breaches": r.json()}
        else:
            return {"email": email, "breaches": "Aucune fuite trouvée"}
    except:
        return {"error": "Erreur API"}
