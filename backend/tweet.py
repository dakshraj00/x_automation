from auth_utils import refresh_token
from main import News
from news import response
import requests, json, time

res=response
def post_tweet():
    global res
    tokens = refresh_token()  # ← only one call
    if not tokens or "access_token" not in tokens:
        print("❌ Failed to refresh token")
        return

    ACCESS_TOKEN = tokens["access_token"]
    print("✅ Got new access token")

    tweet_text = News(res)
    if len(tweet_text) > 280:
        tweet_text = tweet_text[:277] + "..."

    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"text": tweet_text}

    res = requests.post(url, headers=headers, data=json.dumps(payload))
    print("📤 Tweet status:", res.status_code, res.text)
