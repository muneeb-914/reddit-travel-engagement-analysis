import praw
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent='Reddit Trend Analyzer by /u/Pleasant-Coyote-1014'
)


SUBREDDIT_NAME = 'travel'
POST_LIMIT = 100

posts_data = []

subreddit = reddit.subreddit(SUBREDDIT_NAME)

for post in subreddit.hot(limit=POST_LIMIT):
    posts_data.append({
        'post_id': post.id,
        'title': post.title,
        'score': post.score,
        'author': str(post.author),
        'created_utc': datetime.fromtimestamp(post.created_utc),
        'subreddit': SUBREDDIT_NAME,
        'num_comments': post.num_comments
    })

df = pd.DataFrame(posts_data)

df.to_csv('raw_reddit_data.csv', index=False)

print("Reddit data has been successfully fetched and saved to 'raw_reddit_data.csv'.")