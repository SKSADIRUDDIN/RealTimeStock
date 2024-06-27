import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "+17628155548"
VERIFIED_NUMBER = "+917908081701"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "FRA7MO9NTV3VXUII"
NEWS_API_KEY = "44316e7fb285416a8000269579c8d2e3"
TWILIO_SID = "ACcbb13c14f149807407a7efd634f67dfa"
TWILIO_AUTH_TOKEN = "c9f8316cf790ba59debd81121a31fe03"

def send_news():
    # Get yesterday's closing stock price
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]

    # Get the day before yesterday's closing stock price
    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

    # Calculate price difference and percentage change
    difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
    diff_percent = round((difference / float(yesterday_closing_price)) * 100)

    # Determine if the change is significant (> 1%)
    if abs(diff_percent) > 1:
        news_params = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME,
        }

        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]

        # Use Python slice operator to create a list that contains the first 3 articles
        three_articles = articles[:3]

        # Format articles for SMS
        formatted_articles = [
            f"{STOCK_NAME}: {'🔺' if difference > 0 else '🔻'}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
            for article in three_articles
        ]

        # Send each article as a separate message via Twilio
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_='whatsapp:+14155238886',
                to='whatsapp:+917908081701'
            )
            print(f"Message sent: {message.sid}")


