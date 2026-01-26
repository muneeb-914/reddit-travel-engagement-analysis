import pandas as pd

# ============================================================
# Phase 3: Exploratory Data Analysis (EDA)
# Project: Reddit Travel Engagement Analysis
# Objective:
# Analyze engagement patterns to extract actionable insights
# ============================================================


# ------------------------------------------------------------
# 1. Load the dataset
# ------------------------------------------------------------
df = pd.read_csv("data/raw_reddit_data.csv")


# ------------------------------------------------------------
# 2. Create an engagement metric
# Question:
# How can we quantify overall engagement for a post?
# (Engagement = Upvotes + Number of Comments)
# ------------------------------------------------------------
df["engagement"] = df["score"] + df["num_comments"]


# ------------------------------------------------------------
# 3. Question 1:
# Which posts receive the highest engagement?
# ------------------------------------------------------------
top_engagement_posts = (
    df.sort_values(by="engagement", ascending=False)
      .head(10)
)

print("\nTop 10 Posts by Engagement:\n")
print(top_engagement_posts[["title", "score", "num_comments", "engagement"]])


# ------------------------------------------------------------
# 4. Question 2:
# Do posts with more comments also receive more upvotes?
# (Correlation Analysis)
# ------------------------------------------------------------
print("\nCorrelation between Score and Number of Comments:\n")
print(df[["score", "num_comments"]].corr())


# ------------------------------------------------------------
# 5. Time-based Analysis
# Question:
# Does posting time influence engagement?
# ------------------------------------------------------------
df["created_utc"] = pd.to_datetime(df["created_utc"])
df["hour"] = df["created_utc"].dt.hour
df["day_of_week"] = df["created_utc"].dt.day_name()


# --- Average engagement by hour ---
print("\nAverage Engagement by Hour (UTC):\n")
print(
    df.groupby("hour")["engagement"]
      .mean()
      .sort_values(ascending=False)
)


# --- Average engagement by day of week ---
print("\nAverage Engagement by Day of Week:\n")
print(
    df.groupby("day_of_week")["engagement"]
      .mean()
      .sort_values(ascending=False)
)


# ------------------------------------------------------------
# 6. Question 3:
# Engagement Distribution
# Are most posts low-engagement with a few viral ones?
# ------------------------------------------------------------
print("\nEngagement Distribution Summary:\n")
print(df["engagement"].describe())


# Number of posts above average engagement
above_avg = df[df["engagement"] > df["engagement"].mean()].shape[0]
total_posts = df.shape[0]

print(f"\nPosts above average engagement: {above_avg}")
print(f"Total posts analyzed: {total_posts}")