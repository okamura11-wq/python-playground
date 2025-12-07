import pandas as pd

df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])

grouped_store = (
    df.groupby("store", as_index=False)
    ["sales"].sum()
)

pivot_sales = pd.pivot_table(
    df,
    index="date",
    columns="store",
    values="sales",
    aggfunc="sum",
)

df_mi = df.set_index(["store", "item", "date"])
df_score_a = df_mi.xs("A", level="store")
df_swapped = df_mi.swaplevel("store", "item")
df_sorted = df_swapped.sort_index()

print(df.head())
print(grouped_store.head())