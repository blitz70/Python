import pandas as pd
import numpy as np
from statistics import mean


def direction(now, future):
    if future > now:
        return 1
    else:
        return 0


def average(values):
    return mean(values)

hpi = pd.read_pickle("hpi.pickle")
hpi = hpi.pct_change()

hpi.replace([np.inf, -np.inf], np.nan, inplace=True)
hpi["USA_F"] = hpi["USA"].shift(-1)

# function mapping
# hpi["Label"] = (hpi["USA_F"] > hpi["USA"])*1
hpi["Label"] = list(map(direction, hpi["USA"], hpi["USA_F"]))

# rolling apply
# hpi["MORG_M0"] = hpi["MORG"].rolling(10).mean()
# hpi["MORG_M"] = pd.rolling_apply(hpi["MORG"], 10, average)
hpi["MORG_M"] = hpi["MORG"].rolling(10).apply(average)

hpi.dropna(inplace=True)

print(hpi[["USA", "USA_F", "Label", "MORG", "MORG_M"]].head())
