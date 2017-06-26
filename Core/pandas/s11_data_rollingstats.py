import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style


def modify_data():
    for data in HPI_states:
        HPI_states[data] = (HPI_states[data] - HPI_states[data][0]) / HPI_states[data][0] * 100
    HPI_usa["USA"] = (HPI_usa["USA"] - HPI_usa["USA"][0]) / HPI_usa["USA"][0] * 100

key = open("apikey.txt", "r").read()

HPI_states = pd.read_pickle("hpi_states.pickle")
HPI_usa = pd.read_pickle("hpi_usa.pickle")

modify_data()
HPI_states["TX_12MA"] = HPI_states["TX"].rolling(12).mean()
HPI_states["TX_12STD"] = HPI_states["TX"].rolling(12).std()
print(HPI_states[["TX", "TX_12MA", "TX_12STD"]])
TX_AK_12corr = HPI_states["TX"].rolling(12).corr(HPI_states["AK"])

style.use("ggplot")

plt.figure(1)
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)
HPI_states[["TX", "TX_12MA"]].plot(ax=ax1)
HPI_states[["TX_12STD"]].plot(ax=ax2, color="g")

plt.figure(2)
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)
HPI_states[["TX", "AK"]].plot(ax=ax1)
TX_AK_12corr.plot(ax=ax2, color="g", label="TX_AK_12corr")
plt.legend()

plt.show()
