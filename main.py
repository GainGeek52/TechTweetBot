import tweepy
import feedparser
import random
import os
import requests

def summarize_with_openrouter(headline, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": f"Rewrite this tech news headline to be more engaging and tweet-friendly:\n\n{headline}"}
        ],
        "temperature": 0.7,
        "max_tokens": 40
    }

    response = requests.post(url, headers=headers, json=data)
    try:
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("Error in summarization:", e)
        return headline  # fallback to original if summarization fails

# --- Configuration ---
api_key = os.getenv('TWITTER_API_KEY')
api_secret = os.getenv('TWITTER_API_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_SECRET')

HASHTAGS = "#Tech #AI #Innovation #Startup"
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

# --- Input Validation ---
if not all([api_key, api_secret, access_token, access_token_secret, NEWS_API_KEY, OPENROUTER_API_KEY]):
    print("Error: Required API credentials not found.")
    print("Please set TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, and NEWS_API_KEY environment variables.")
    exit(1)

# --- Twitter Authentication (API v2) ---
try:
    print("Authenticating with Twitter API v2...")
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    print("Authentication successful!")
except tweepy.errors.TweepyException as e:
    print(f"Error during Twitter authentication: {e}")
    exit(1)

# --- Fetch and Select Article ---
try:
    url = f'https://newsapi.org/v2/top-headlines?category=technology&language=en&pageSize=5&apiKey={NEWS_API_KEY}'
    print("Fetching articles from NewsAPI...")
    response = requests.get(url).json()
    
    if 'articles' not in response or not response['articles']:
        print("Error: No articles found in the NewsAPI response.")
        print(f"API Response: {response}")
        exit(1)

    article = random.choice(response['articles'])
    original_title = article['title']
    title = summarize_with_openrouter(original_title, OPENROUTER_API_KEY)
    link = article['url']
    print(f"Original title: '{original_title}'")
    print(f"Summarized title: '{title}'")
except Exception as e:
    print(f"Error fetching or parsing RSS feed: {e}")
    exit(1)

# --- Compose Tweet ---
opening_phrases = [
    "Just in! 📣",
    "Breaking news! 🗞",
    "Check this out:",
    "Interesting read 👀",
    "Hot off the press:",
    "You won't believe this!",
    "Must-read alert 📱",
    "Tech update 🔄"
]

ending_phrases = [
    "Thoughts? 🤔",
    "What do you think?",
    "Read more here ⬇",
    "Fascinating stuff!",
    "Game-changer? 🎯",
    "Mind = blown 🤯"
]

random_opener = random.choice(opening_phrases)
random_ending = random.choice(ending_phrases)

tweet = f"{random_opener} {title}\n\n{random_ending}\n🔗 {link}\n\n{HASHTAGS}"
if len(tweet) > 280:
    available_chars = 280 - len(f"{random_opener} ...\n\n{random_ending}\n🔗 {link}\n\n{HASHTAGS}") - 3
    truncated_title = title[:available_chars] + "..."
    tweet = f"{random_opener} {truncated_title}\n\n{random_ending}\n🔗 {link}\n\n{HASHTAGS}"

# --- Post Tweet ---
print("\nAttempting to post tweet:")
print("---")
print(tweet)
print("---")

try:
    response = client.create_tweet(text=tweet)
    print("\nSuccessfully tweeted!")
    print(f"Tweet ID: {response.data['id']}")
except tweepy.errors.TweepyException as e:
    print(f"\nError posting tweet: {e}")
    # Common errors:
    # - [403 Forbidden] 187 - Status is a duplicate.
    # - [403 Forbidden] ... - Read-only application cannot POST. (Check app permissions)
    # - [401 Unauthorized] ... - Invalid/expired token or bad authentication. (Check credentials)
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")