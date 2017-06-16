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
                    'Int_rate': [2, 3, 2, 2],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index=[2001, 2002, 2003, 2004])

df4 = pd.concat([df1, df2])
df4 = pd.concat([df1, df2, df3])

df4 = df1.append(df2)
df4 = df1.append(df3)

s = pd.Series([80, 2, 50])
df4 = df1.append(s, ignore_index=True)
print(df4)
s = pd.Series([80, 2, 50], index=["HPI", "Int_rate", "US_GDP_Thousands"])
df4 = df1.append(s, ignore_index=True)

print(df4)
