import requests
import os
from dotenv import load_dotenv

load_dotenv("config.env")

NGROK_STATUS_URL = os.getenv("NGROK_API", "http://127.0.0.1:4040/api/tunnels")
TEMPLATE_FILE = "index_template.html"
OUTPUT_FILE = "index.html"

def get_ngrok_https_url():
    try:
        tunnels = requests.get(NGROK_STATUS_URL).json()['tunnels']
        for tunnel in tunnels:
            if tunnel['proto'] == 'https':
                return tunnel['public_url']
    except Exception as e:
        print("Erreur Ngrok :", e)
    return None

def update_html(url):
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()
    content = template.replace("https://VOTRE_URL_NGROK.io", url)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ index.html mis à jour vers {url}")

if __name__ == "__main__":
    public_url = get_ngrok_https_url()
    if public_url:
        update_html(public_url)
    else:
        print("❌ Impossible de récupérer l’URL Ngrok.")
