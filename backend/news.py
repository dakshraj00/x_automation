import requests
import os 
from dotenv import load_dotenv

load_dotenv()

# 🔑 Your API key
API_KEY = os.getenv("NEWS_API")

# 🔗 NewsAPI endpoint for top headlines
url = "https://newsapi.org/v2/top-headlines"

# 🧩 Parameters for tech news
params = {
    "category": "technology",   # You can also use 'business', 'science', etc.
    "language": "en",           # English articles only
    "pageSize": 5,              # Number of top results
    "apiKey": API_KEY
}

# 📡 Fetch data
response = requests.get(url, params=params)

# ✅ Check success

def Fetch_news(response):
    if response.status_code==200:
        data=response.json()
        articles=data['articles']
        
        news_list=[]
        for idx,article in enumerate(articles,2):
            news_item={
                "Index":idx,
                "Title":article["title"],
                "Source":article['source']['name'],
                "URL":article["url"]


            }
            news_list.append(news_item)
        return news_list
            
    else:
        return {f'An error occured {response.status_code}'}

