import pandas as pd

df1 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index=[2001, 2002, 2003, 2004])

df4 = pd.merge(df1, df2, on=["HPI"])

df1.set_index("HPI", inplace=True)
df3.set_index("HPI", inplace=True)
df4 = df1.join(df3)

# print(df4)

df5 = pd.DataFrame({"Year": [2001, 2002, 2003, 2004],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},)

df6 = pd.DataFrame({"Year": [2001, 2003, 2004, 2005],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53]},)

# inner
# df7 = pd.merge(df5, df6, on="Year") # default
# df7.set_index("Year", inplace=True)
# df5.set_index("Year", inplace=True)
# df6.set_index("Year", inplace=True)
# df8 = df5.join(df6, how="inner")

# left
# df7 = pd.merge(df5, df6, on="Year", how="left")
# df7.set_index("Year", inplace=True)
# df5.set_index("Year", inplace=True)
# df6.set_index("Year", inplace=True)
# df8 = df5.join(df6, how="left") # default

# right
# df7 = pd.merge(df5, df6, on="Year", how="right")
# df7.set_index("Year", inplace=True)
# df5.set_index("Year", inplace=True)
# df6.set_index("Year", inplace=True)
# df8 = df5.join(df6, how="right")

# outer
df7 = pd.merge(df5, df6, on="Year", how="outer")
df7.set_index("Year", inplace=True)
df5.set_index("Year", inplace=True)
df6.set_index("Year", inplace=True)
df8 = df5.join(df6, how="outer")

print(df7)
print(df8)
