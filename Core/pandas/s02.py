import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

web_stats = {
    "Day": [1, 2, 3, 4, 5, 6],
    "Visitors": [43, 53, 34, 45, 64, 34],
    "Bounce_Rate": [65, 72, 62, 64, 54, 66],
}
df = pd.DataFrame(web_stats)

print(df)
print(df.head())
print(df.tail())
print(df.tail(2))

df2 = df.set_index("Day")
print(df)
print(df2)
df.set_index("Day", inplace=True)
print(df)

print(df["Visitors"])
print(df.Visitors)
print(df[["Visitors", "Bounce_Rate"]])

df_to_list = df["Visitors"].tolist()
print(df_to_list)
df_to_array = np.array(df[["Visitors", "Bounce_Rate"]])
print(df_to_array)
print("="*30)
array_to_df = pd.DataFrame(df_to_array)
print(array_to_df)

