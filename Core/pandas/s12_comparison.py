import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

bridge_height = {
    "meters": [10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]
}

bridge_df = pd.DataFrame(bridge_height)
bridge_df["STD"] = bridge_df["meters"].rolling(2).std()

print(bridge_df)
print(bridge_df.describe())
print(bridge_df.describe()["meters"]["std"])
bridge_df = bridge_df[bridge_df["STD"] < bridge_df.describe()["meters"]["std"]]
print(bridge_df)

bridge_df["meters"].plot()
plt.show()
