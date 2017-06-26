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
HPI_states["TX_YR"] = HPI_states["TX"].resample("A").mean()

style.use("ggplot")

plot_data = HPI_states.dropna()
plot_data[["TX", "TX_YR"]].plot()

plot_data = HPI_states.fillna(method="ffill")
plot_data[["TX", "TX_YR"]].plot()

plot_data = HPI_states.fillna(method="bfill")
plot_data[["TX", "TX_YR"]].plot()

plot_data = HPI_states.fillna(value=0)
plot_data[["TX", "TX_YR"]].plot()

plt.show()
