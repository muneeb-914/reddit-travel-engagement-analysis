# Reddit Data Analysis Project

## Overview
This project analyzes Reddit posts to understand engagement patterns, posting behavior, and content performance. It is designed as an end-to-end **data analysis portfolio project**, moving step by step from raw data collection to analysis and visualization.

The project is intentionally structured in **phases** to show clear thinking, clean workflow, and real-world analytical practice.

---

## Tech Stack
- **Python** (Data collection & analysis)
- **Pandas, NumPy** (Data manipulation)
- **Reddit API (PRAW)** (Data extraction)
- **Power BI** (Final visualization & dashboard)
- **GitHub** (Version control & documentation)

---

## Phase 1: Data Collection

**Goal:** Collect raw Reddit post data using the Reddit API.

### What was done
- Connected to Reddit using PRAW
- Extracted post-level data such as:
  - Post ID
  - Title
  - Subreddit
  - Score (upvotes)
  - Number of comments
  - Created date
- Stored the collected data in a CSV file for further analysis

**Output:**
- `reddit_posts_raw.csv`

---

## Phase 2: Data Cleaning & Preparation

**Goal:** Make the raw data usable and analysis-ready.

### What was done
- Converted timestamps into readable datetime format
- Checked and handled missing or inconsistent values
- Ensured correct data types for numerical and date columns
- Removed unnecessary fields

---

## Phase 3: Exploratory Data Analysis (EDA)

**Goal:** Understand engagement patterns and post behavior.

### Key Questions Answered
- How are post scores distributed?
- Are most posts low-engagement with a few viral ones?
- What is the relationship between score and number of comments?
- Which subreddits show higher engagement?
- How does posting time affect engagement?

### What was done
- Analyzed distributions of scores and comments
- Identified skewness in engagement (many low, few very high)
- Explored correlations between engagement metrics
- Created derived columns where needed for analysis (without modifying the original cleaned CSV)

**Key Insight:**
Reddit engagement follows a **long-tail distribution**, where most posts receive low engagement and a small number of posts go viral.

---

## Phase 4: Visualization (Power BI)

**Goal:** Communicate insights visually using an industry-standard BI tool.

### Visualizations Created
- Distribution of post scores
- Engagement comparison across subreddits
- Score vs comments relationship
- Posting time vs engagement

### Tools
- **Power BI** was used instead of Python visualization libraries to reflect real-world analyst workflows.

**Output:**
- Interactive Power BI dashboard

---

## Project Structure
```
├── data/
│   ├── reddit_posts_raw.csv
├── notebooks/
│   ├── data_collection.py
│   ├── eda.py
├── powerbi/
│   ├── report.pbix
├── README.md

```

---

## Key Learnings
- Working with real APIs and messy data
- Structuring analysis in clear phases
- Translating raw numbers into insights
- Using Power BI for professional dashboards
- Writing clean, understandable project documentation

---

## Next Steps
- Add more subreddits for comparison
- Perform sentiment analysis on post titles
- Automate data refresh using scheduled scripts

---

## Author
**Muneeb**
Aspiring Data Analyst | Python | SQL | Power BI

---

*This project is part of my data analysis learning journey and portfolio.*

