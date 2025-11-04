import requests
import base64
import os
from dotenv import load_dotenv, set_key

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
ENV_PATH = ".env"

def refresh_token():
    url = "https://api.twitter.com/2/oauth2/token"

    # 🧠 Proper Authorization header
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_header}"
    }

    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        tokens = response.json()
        print("🔑 Refreshed token:", tokens)

        new_refresh = tokens.get("refresh_token")
        if new_refresh:
            # ✅ Dynamically update .env safely
            set_key(ENV_PATH, "REFRESH_TOKEN", new_refresh)
            print("✅ Updated .env with new refresh token")

            # ✅ Update in-memory environment too
            os.environ["REFRESH_TOKEN"] = new_refresh

        return tokens
    else:
        print("❌ Token refresh failed:", response.status_code, response.text)
        return None


if __name__ == "__main__":
    refresh_token()
