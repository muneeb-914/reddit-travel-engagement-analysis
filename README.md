### 🔹 Project Overview

This project analyzes engagement patterns in Reddit travel-related posts. The goal is to extract, structure, and analyze Reddit data to understand what type of travel content receives the highest user engagement.

### 🔹 Business Objective

* The objective of this project is to answer the following questions:
* What travel-related posts receive the most engagement on Reddit?
* How active is the subreddit based on post volume?
* Which posts generate the most discussion?

### 🔹 Phase 1: Project Scope \& Planning

* Selected subreddit: r/travel
* Data source: Reddit API
* Focus metrics:
* Upvotes (score)
* Number of comments
* Output format: CSV for Power BI visualization

### 🔹 Phase 2: Data Collection

* Extracted 100 posts using the Reddit API via PRAW
* Collected post-level data including:
* Post ID
* Title
* Author
* Score
* Number of comments
* Created timestamp
* Stored raw data in raw\_reddit\_data.csv for further processing

#### 🔹 Tools Used

* Python
* PRAW (Reddit API)
* Pandas
* Power BI (planned)