
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Forecasting Dashboard")
st.write("Online Retail Sales Analysis")

df = pd.read_csv("daily_sales.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"£{df['DailySales'].sum():,.0f}")
col2.metric("Average Daily Sales", f"£{df['DailySales'].mean():,.0f}")
col3.metric("Total Days", len(df))

st.subheader("Daily Sales Trend")
fig = px.line(df, x="InvoiceDate", y="DailySales", title="Daily Revenue")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Monthly Sales")
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
monthly = df.groupby("Month", as_index=False)["DailySales"].sum()

fig2 = px.bar(monthly, x="Month", y="DailySales", title="Monthly Revenue")
st.plotly_chart(fig2, use_container_width=True)
