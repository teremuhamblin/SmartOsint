import phonenumbers
from phonenumbers import geocoder, carrier

def phone_lookup(number):
    try:
        num = phonenumbers.parse(number)
        return {
            "number": number,
            "country": geocoder.description_for_number(num, "fr"),
            "carrier": carrier.name_for_number(num, "fr")
        }
    except:
        return {"error": "Numéro invalide"}
