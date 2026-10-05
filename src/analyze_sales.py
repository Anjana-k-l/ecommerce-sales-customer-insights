import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "ecommerce_sales.csv"
OUT = ROOT / "reports"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)

summary = {
    "orders": int(df["order_id"].nunique()),
    "customers": int(df["customer_id"].nunique()),
    "revenue": round(df["sales"].sum(), 2),
    "profit": round(df["profit"].sum(), 2),
    "profit_margin_pct": round(df["profit"].sum() / df["sales"].sum() * 100, 2),
    "avg_order_value": round(df.groupby("order_id")["sales"].sum().mean(), 2),
}

monthly = df.groupby("month", as_index=False).agg(sales=("sales", "sum"), profit=("profit", "sum"))
category = df.groupby("category", as_index=False).agg(sales=("sales", "sum"), profit=("profit", "sum"), orders=("order_id", "nunique"))
region = df.groupby("region", as_index=False).agg(sales=("sales", "sum"), profit=("profit", "sum"), orders=("order_id", "nunique"))

monthly.to_csv(OUT / "monthly_kpis.csv", index=False)
category.to_csv(OUT / "category_kpis.csv", index=False)
region.to_csv(OUT / "region_kpis.csv", index=False)

with open(OUT / "executive_summary.md", "w", encoding="utf-8") as f:
    f.write("# Executive Summary\n\n")
    for k,v in summary.items(): f.write(f"- **{k.replace('_',' ').title()}**: {v}\n")
    f.write("\n## Key observations\n")
    f.write(f"- Top category by sales: **{category.sort_values('sales', ascending=False).iloc[0]['category']}**.\n")
    f.write(f"- Top region by sales: **{region.sort_values('sales', ascending=False).iloc[0]['region']}**.\n")
    f.write(f"- Highest-margin category: **{(category.assign(margin=category.profit/category.sales).sort_values('margin', ascending=False).iloc[0]['category'])}**.\n")

print(summary)
