import praw
import pandas as pd
from datetime import datetime

reddit = praw.Reddit(
    client_id='jKgfBmNXgaPya5PRry3Fow',
    client_secret='QI6447ONGZ4-2-etfeUeaEO-H0xCpA',
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

df ["created_utc"] = pd.to_datetime(df['created_utc'])

df ["date"] = df["created_utc"].dt.date

# df.to_csv('raw_reddit_data.csv', index=False)

# print("Reddit data has been successfully fetched and saved to 'raw_reddit_data.csv'.")

df ['engagement'] = df['score'] + df['num_comments']

top_posts = df.sort_values(by="engagement",ascending=False).head(10)

#print(top_posts[["title", "score", "num_comments", "engagement"]])


# print(df[["score", "num_comments", "engagement"]].head())


# print(df.dtypes)

df['hours'] = df['created_utc'].dt.hour
df['days_of_week'] = df['created_utc'].dt.day_name()

print(df[['created_utc','hours', 'days_of_week']].head())