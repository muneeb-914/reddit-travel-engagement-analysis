### \# Reddit Travel Engagement Analysis

### 

### A data analysis project focused on understanding engagement patterns within the \*\*r/travel\*\* subreddit. This project extracts data via the Reddit API, processes it using Python, and prepares it for visualization to uncover what drives travel-related discussions.

### 

### ---

### 

### \## 📌 Project Overview

### The goal is to analyze what type of travel content receives the highest user interaction. By examining scores, comment counts, and posting times, this project identifies the "signals" behind high-performing posts.

### 

### \### Business Objectives

### \* Identify travel-related topics with the most engagement.

### \* Measure subreddit activity levels based on post volume.

### \* Pinpoint which posts generate the most discussion vs. just upvotes.

### 

### ---

### 

### \## 🛠️ Tech Stack

### \* \*\*Python\*\* (Core Analysis)

### \* \*\*PRAW\*\* (Reddit API Wrapper)

### \* \*\*Pandas\*\* (Data Manipulation)

### \* \*\*Power BI\*\* (Planned for Dashboards)

### 

### ---

### 

### \## 📂 Project Phases

### 

### \### Phase 1: Planning

### \* \*\*Source:\*\* r/travel via Reddit API.

### \* \*\*Metrics:\*\* Score (upvotes), comment count, and timestamps.

### \* \*\*Output:\*\* Structured CSV for analysis.

### 

### \### Phase 2: Data Collection

### \* Extracted 100 posts using \*\*PRAW\*\*.

### \* Saved raw data to `raw\_reddit\_data.csv`.

### \* Fields collected: Post ID, Title, Author, Score, Comments, and UTC Timestamp.

### 

### \### Phase 3: Exploratory Data Analysis (EDA)

### This is where the raw data is transformed into insights.

### 

### \*\*Feature Engineering:\*\*

### Created a custom `engagement` metric:

### `engagement = score + num\_comments`

### 

### \*\*Key Analysis Performed:\*\*

### 1\. \*\*Engagement Leaders:\*\* Identifying the Top 10 posts.

### 2\. \*\*Correlation:\*\* Checking the relationship between upvotes and comment volume.

### 3\. \*\*Time Analysis:\*\* Grouping engagement by hour of the day and day of the week to find peak posting times.

### 4\. \*\*Distribution:\*\* Using descriptive stats to see how "rare" high-performing posts actually are.

### 

### ---

### 

### \## 📈 Key Insights (So Far)

### \* High engagement isn't just about upvotes; comments are a major driver of interaction.

### \* Posting time (hour/day) significantly impacts how much visibility a post gets.

### \* Only a small percentage of posts perform above the average engagement threshold.

### 

### 

