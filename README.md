# E-Commerce Sales & Customer Insights Dashboard

A portfolio-ready Data Analyst project built with Python, Pandas, SQL (SQLite), and Streamlit. The project cleans and analyzes **12,000 synthetic e-commerce transactions** and turns them into business KPIs and visual insights.

## Business questions
- How is revenue changing month over month?
- Which product categories and regions contribute the most revenue?
- Which categories have the strongest profit margins?
- What is the average order value?
- Which customers show repeat-purchase behavior?

## Project structure
```text
data/             synthetic transaction dataset
sql/              reusable SQL analysis queries
src/              Python KPI/ETL analysis script
reports/          generated KPI tables and executive summary
dashboard.py      Streamlit dashboard
requirements.txt  Python dependencies
```

## Run the analysis
```bash
python src/analyze_sales.py
```

## Run the dashboard
```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## Data note
The dataset is synthetic and was generated for portfolio/learning purposes. No real customer data is included.

## Skills demonstrated
Python, Pandas, NumPy, SQL, SQLite, data cleaning, exploratory data analysis, KPI analysis, aggregation, business insights, data visualization, Git, GitHub, Streamlit, Plotly.
