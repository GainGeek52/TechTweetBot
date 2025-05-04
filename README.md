# 📣 TechTweetBot

**TechTweetBot** is an automated Twitter bot that fetches the latest technology news, rewrites headlines into tweet-friendly formats using OpenRouter (GPT-3.5-Turbo), and posts them to Twitter with relevant hashtags.

---

## 🚀 Features

- 🔍 Fetches top tech headlines using NewsAPI  
- 🤖 Summarizes and rewrites headlines using OpenRouter (GPT-3.5-Turbo)  
- 🐦 Tweets with opening/ending phrases for engagement  
- 🔗 Includes article links and hashtags  
- ✅ Ensures tweet fits within the 280-character limit  

---

## 🛠️ Requirements

- Python 3.7+  
- Twitter Developer Account (for API keys)  
- NewsAPI account (free)  
- OpenRouter API key (free or paid)  

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/techtweetbot.git
   cd techtweetbot

**Install dependencies**

   ```bash
   pip install tweepy requests feedparser python-dotenv
   ```

**Create a `.env` file**

   Add your API keys to a new `.env` file in the root directory:

   ```ini
   TWITTER_API_KEY=your_key
   TWITTER_API_SECRET=your_secret
   TWITTER_ACCESS_TOKEN=your_token
   TWITTER_ACCESS_SECRET=your_token_secret
   NEWS_API_KEY=your_newsapi_key
   OPENROUTER_API_KEY=your_openrouter_key
   ```

**Run the bot**

   ```bash
   python bot.py
   ```

---

## 🧠 Example Output

```text
Just in! 📣 AI startup breaks new ground in synthetic speech technology

Fascinating stuff!
🔗 https://example.com/article-link

#Tech #AI #Innovation #Startup
```

---

## 💡 Project Name Suggestions

* **TechTweetBot** *(Simple & direct)*
* **AutoTechTweeter**
* **SmartNewsBot**
* **DailyTechBuzz**
* **TweetifyTech**
* **TechWhisperer**

---

## 📝 Customization Ideas

* Add support for image thumbnails from article metadata
* Schedule tweets at intervals using `cron` or `APScheduler`
* Track posted URLs to avoid duplication
* Use more AI models (e.g., Claude, Mixtral) via OpenRouter
* Add multi-language tweet support
