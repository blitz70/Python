import pandas as pd


df = pd.read_csv("ZILL-Z77006_3B.csv")

df.set_index("Date", inplace=True)

df.to_csv("2.csv")
# df["Value"].to_csv("2.csv")

df = pd.read_csv("2.csv")

df = pd.read_csv("2.csv", index_col="Date")

df.columns = ["House_Price"]

#df.to_csv("3.csv")
df.to_csv("3.csv", header=False)

df = pd.read_csv("3.csv", names=["Data", "House_Price"], index_col=0)

df.to_html("3.html")

df.rename(columns={"House_Price": "Price"}, inplace=True)

print(df.head())
