# Stockify

This project fetches stock data from Alpha Vantage, retrieves news related to a specific company using the News API, and sends notifications via Twilio's API.

---

## Overview

This project aims to provide real-time updates on stock prices and related news for a specified company. It fetches yesterday's and the day before yesterday's closing stock prices, calculates the price difference and percentage change, retrieves relevant news articles, and sends the top three articles as notifications via Twilio messages.

---

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   pip install requests twilio
   python script_name.py

## API Keys

1. Before running the script, you need to obtain API keys for the following services:

```plaintext
STOCK_API_KEY = "your_alpha_vantage_api_key"
NEWS_API_KEY = "your_news_api_key"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
