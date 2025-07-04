import requests
import os

def fetch_latest_info(query: str) -> str:
    api_key = os.getenv("NEWSAPI_KEY")
    params = {
        "q": query,
        "apiKey": api_key,  
    }
    url = "https://newsapi.org/v2/everything"
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Error fetching news: {response.text}"

    articles = response.json().get("articles", [])
    if articles:
        return f"Live news: {articles[0]['title']} - {articles[0]['description']}"
    return "No relevant news found."
