import requests
import time
import os
from dotenv import load_dotenv

load_dotenv("config.env")

DUCKDNS_DOMAIN = os.getenv("DUCKDNS_DOMAIN")
DUCKDNS_TOKEN = os.getenv("DUCKDNS_TOKEN")
NGROK_STATUS_URL = os.getenv("NGROK_API")

def get_ngrok_https_url():
    try:
        tunnels = requests.get(NGROK_STATUS_URL).json()['tunnels']
        for tunnel in tunnels:
            if tunnel['proto'] == 'https':
                return tunnel['public_url']
    except Exception as e:
        print(f"Erreur récupération Ngrok: {e}")
    return None

def update_duckdns_txt(ip_or_url):
    url = f"https://www.duckdns.org/update?domains={DUCKDNS_DOMAIN}&token={DUCKDNS_TOKEN}&txt={ip_or_url}&verbose=true"
    r = requests.get(url)
    print(f"DuckDNS update : {r.text}")

while True:
    public_url = get_ngrok_https_url()
    if public_url:
        update_duckdns_txt(public_url)
        print(f"Redirigé vers : {public_url}")
        break
    else:
        print("Ngrok pas encore lancé, attente...")
        time.sleep(3)
