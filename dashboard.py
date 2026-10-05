import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

DATA = Path(__file__).parent / 'data' / 'ecommerce_sales.csv'
df = pd.read_csv(DATA, parse_dates=['order_date'])
df['month'] = df['order_date'].dt.to_period('M').astype(str)

st.set_page_config(page_title='E-Commerce Sales Dashboard', layout='wide')
st.title('E-Commerce Sales & Customer Insights Dashboard')
st.caption('Portfolio project using synthetic transaction data.')

region = st.sidebar.multiselect('Region', sorted(df['region'].unique()), default=sorted(df['region'].unique()))
category = st.sidebar.multiselect('Category', sorted(df['category'].unique()), default=sorted(df['category'].unique()))
f = df[df['region'].isin(region) & df['category'].isin(category)].copy()

orders = f['order_id'].nunique(); customers = f['customer_id'].nunique(); revenue = f['sales'].sum(); profit = f['profit'].sum()
aov = f.groupby('order_id')['sales'].sum().mean()

c1,c2,c3,c4 = st.columns(4)
c1.metric('Orders', f'{orders:,}')
c2.metric('Customers', f'{customers:,}')
c3.metric('Revenue', f'₹{revenue:,.0f}')
c4.metric('Avg Order Value', f'₹{aov:,.0f}')

monthly = f.groupby('month', as_index=False)['sales'].sum()
cat = f.groupby('category', as_index=False)['sales'].sum().sort_values('sales', ascending=False)
reg = f.groupby('region', as_index=False)['sales'].sum().sort_values('sales', ascending=False)

st.plotly_chart(px.line(monthly, x='month', y='sales', title='Monthly Revenue'), use_container_width=True)
st.plotly_chart(px.bar(cat, x='category', y='sales', title='Revenue by Category'), use_container_width=True)
st.plotly_chart(px.bar(reg, x='region', y='sales', title='Revenue by Region'), use_container_width=True)
