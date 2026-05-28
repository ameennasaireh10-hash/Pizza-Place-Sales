Pizza Business Command Center 🍕

This project is an end-to-end Data Science application designed to transform raw pizza sales data into actionable business intelligence. It provides restaurant owners with real-time insights, sales trends, and AI-powered product recommendations to optimize menu performance and increase revenue.


Project Goal

This project was developed to engage with the data market early and apply machine learning concepts to solve real-world business problems, moving from raw data to a functional decision-making tool.


Key Features

KPI Dashboard: Real-time monitoring of Total Revenue, Total Orders, and Average Order Value (AOV).


Sales Trends: Interactive visualization of top-performing pizza products using Plotly.


AI Combo Recommendations: Uses the Apriori Algorithm (Association Rule Mining) to automatically identify items frequently bought together and calculate their "Lift" metrics.


Dynamic Insights: The system processes data automatically, ensuring recommendations reflect current sales patterns.


Tech Stack

Language: Python


Data Processing: Pandas


Dashboarding: Streamlit


Visualization: Plotly


Machine Learning: Mlxtend (Apriori Algorithm)


How to Run

Clone this repository:


Bash

git clone [your-github-link]

Install the required dependencies:


Bash

pip install -r requirements.txt

Run the application:


Bash

streamlit run app.py

Methodology

The project follows a standard Data Science pipeline:


Data Cleaning & Integration: Merging disparate CSV files into a unified dataset.


Exploratory Data Analysis (EDA): Identifying key performance indicators and sales trends.


Market Basket Analysis: Applying association rule mining to extract hidden purchase patterns.
