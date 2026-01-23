import pandas as pd
from datetime import datetime
df = pd.read_csv('data/raw_reddit_data.csv')

df ['engagement'] = df['score'] + df['num_comments']
# top_engagement_posts = df.sort_values(
#     by="engagement", ascending=False
# ).head(10)

# print(top_engagement_posts[["title", "score", "num_comments", "engagement"]])


# df[["score", "num_comments"]].corr()

# print(df[["score", "num_comments"]].corr())

df ["created_utc"] = pd.to_datetime(df['created_utc'])
df ["hours"] = df["created_utc"].dt.hour
df ["days_of_week"] = df["created_utc"].dt.day_name()


print(df.groupby("hours")["engagement"].mean().sort_index(ascending=False))
