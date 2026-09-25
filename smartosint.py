import argparse
from modules.phone_lookup import phone_lookup
from modules.email_lookup import email_lookup
from modules.ip_geoloc import ip_geoloc
from modules.device_info import device_info

parser = argparse.ArgumentParser(description="SMARTOSINT v1.0 - OSINT smartphone simple")

parser.add_argument("--number", help="Numéro de téléphone")
parser.add_argument("--email", help="Adresse email")
parser.add_argument("--ip", help="Adresse IP")
parser.add_argument("--model", help="Modèle du smartphone")

args = parser.parse_args()

if args.number:
    print(phone_lookup(args.number))

if args.email:
    print(email_lookup(args.email))

if args.ip:
    print(ip_geoloc(args.ip))

if args.model:
    print(device_info(args.model))
