from fastapi import FastAPI, Request
import requests, base64

app = FastAPI()

CLIENT_ID = "aU9NOUxOLTRSVzFMaWVkVm1QT2M6MTpjaQ"
CLIENT_SECRET = "D1pZpXE-bNMdnMZ5N7O0_ABU1AujyZC5w5YnJvhJj5fBMBVXug"
REDIRECT_URI = "http://localhost:8000/callback"

@app.get("/login")
def login():
    auth_url = (
        f"https://twitter.com/i/oauth2/authorize"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=tweet.read%20tweet.write%20users.read%20offline.access"
        f"&state=random_state"
        f"&code_challenge=challenge"
        f"&code_challenge_method=plain"
    )
    return {"url": auth_url}


@app.get("/callback")
def callback(request: Request):
    code = request.query_params.get("code")
    token_url = "https://api.twitter.com/2/oauth2/token"

    creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_creds = base64.b64encode(creds.encode()).decode()

    data = {
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
        "code_verifier": "challenge"
    }

    headers = {
        "Authorization": f"Basic {b64_creds}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(token_url, data=data, headers=headers)
    tokens = response.json()
    print("✅ Access Token:", tokens.get("access_token"))
    print("🔁 Refresh Token:", tokens.get("refresh_token"))
    return tokens
