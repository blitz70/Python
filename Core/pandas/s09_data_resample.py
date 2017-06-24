import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style


def state_list():
    _state_list = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
    return _state_list[0][0][1:]


def make_data():
    states = state_list()
    states_df = pd.DataFrame()
    for state in states:
        query = "".join(["FMAC/HPI_", state])
        state_df = quandl.get(query, api_key=key)
        state_df.rename(columns={"Value": str(state)}, inplace=True)
        if states_df.empty:
            states_df = state_df
        else:
            states_df = states_df.join(state_df)
    return states_df


def benchmark_data():
    df = quandl.get("FMAC/HPI_USA", api_key=key)
    df.rename(columns={"Value": "USA"}, inplace=True)
    return df

# data analysis : do housing price index(HPI) behave similarly?

key = open("apikey.txt", "r").read()

# print("make data")
# hpi_states = make_data()
# hpi_usa = benchmark_data()
#
# print("save data")
# hpi_states.to_pickle("hpi_states.pickle")
# hpi_usa.to_pickle("hpi_usa.pickle")

print("load data")
HPI_states = pd.read_pickle("hpi_states.pickle")
HPI_usa = pd.read_pickle("hpi_usa.pickle")
# print(HPI_states.head())
# print(HPI_states.describe())

print("modify data")
HPI_states2 = HPI_states.pct_change()
HPI_states3 = pd.DataFrame()
for data in HPI_states:
    HPI_states3[data] = (HPI_states[data]-HPI_states[data][0])/HPI_states[data][0]*100
HPI_usa["USA"] = (HPI_usa["USA"]-HPI_usa["USA"][0])/HPI_usa["USA"][0]*100

# print("data correlation")
# HPI_states_correlate = HPI_states.corr()
# print(HPI_states_correlate)
# print(HPI_states_correlate.describe())

print("resample data")
# HPI_TX_YR = HPI_states["TX"].resample("A").mean()
HPI_TX_YR = HPI_states["TX"].resample("AS").ohlc()
print(HPI_TX_YR)
print(type(HPI_TX_YR))

print("plot data")
style.use("ggplot")
# HPI_states.plot()
# plt.legend().remove()
# HPI_states2.plot()
# plt.legend().remove()
# ax = HPI_states3.plot()
# plt.legend().remove()
# HPI_usa.plot(ax=ax, color="k", linewidth=3)
ax = HPI_states["TX"].plot(label="TX-Month", linewidth=3)
HPI_TX_YR.plot(ax=ax, label="TX-Year")
plt.legend(loc=4)
plt.show()
