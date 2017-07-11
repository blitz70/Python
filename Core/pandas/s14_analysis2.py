import pandas as pd
import quandl
from matplotlib import pyplot as plt
from matplotlib import style


def state_list():
    _state_list = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
    return _state_list[0][0][1:]


def hpi_states_data():
    states = state_list()
    df = pd.DataFrame()
    for state in states:
        query = "".join(["FMAC/HPI_", state])
        _df = quandl.get(query, api_key=key)
        _df["Value"] = (_df["Value"]-_df["Value"][0]) / _df["Value"][0] * 100.0
        _df.rename(columns={"Value": str(state)}, inplace=True)
        if df.empty:
            df = _df
        else:
            df = df.join(_df)
    return df


def hpi_usa_data():
    df = quandl.get("FMAC/HPI_USA", api_key=key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df.rename(columns={"Value": "USA"}, inplace=True)
    return df


def morg_usa_data():
    df = quandl.get("FMAC/30US", trim_start="1975-01-01", api_key=key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df.rename(columns={"Value": "MORG"}, inplace=True)
    df = df.resample("M").mean()
    return df


def sp500_data():
    df = quandl.get("MULTPL/SP500_INFLADJ_MONTH", trim_start="1975-01-01", api_key=key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df.rename(columns={"Value": "SP500"}, inplace=True)
    # df = df.resample('1D').mean()
    df = df.resample('M').mean()
    return df


def gdp_usa_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", api_key=key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df.rename(columns={"Value": "GDP"}, inplace=True)
    return df


def unemployment_usa_data():
    df = quandl.get("USMISERY/INDEX", trim_start="1975-01-01", api_key=key)
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df.rename(columns={"Unemployment Rate": "UNEMPLOYMENT"}, inplace=True)
    df = df[["UNEMPLOYMENT"]]
    return df


key = open("apikey.txt", "r").read()

# print("make data")
# hpi_states = hpi_states_data()
# hpi_usa = hpi_usa_data()
# morg_usa = morg_usa_data()
# sp500 = sp500_data()
# gdp_usa = gdp_usa_data()
# unemployment_usa = unemployment_usa_data()

# print("save data")
# hpi_states.to_pickle("hpi_states.pickle")
# hpi_usa.to_pickle("hpi_usa.pickle")
# morg_usa.to_pickle("morg_usa.pickle")
# sp500.to_pickle("sp500.pickle")
# gdp_usa.to_pickle("gdp_usa.pickle")
# unemployment_usa.to_pickle("unemployment_usa.pickle")

print("load data")
hpi_states = pd.read_pickle("hpi_states.pickle")
hpi_usa = pd.read_pickle("hpi_usa.pickle")
morg_usa = pd.read_pickle("morg_usa.pickle")
sp500 = pd.read_pickle("sp500.pickle")
gdp_usa = pd.read_pickle("gdp_usa.pickle")
unemployment_usa = pd.read_pickle("unemployment_usa.pickle")

# print(hpi_states.head())
# print(hpi_usa.head())
# print(morg_usa.head())
# print(sp500.head())
# print(gdp_usa.head())
# print(unemployment_usa.head())

# HPI = hpi_usa.join([morg_usa, sp500, gdp_usa, unemployment_usa]).dropna()
# HPI.to_pickle("hpi.pickle")
HPI = pd.read_pickle("hpi.pickle")

style.use("ggplot")
HPI.plot()
plt.figure(2)
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)
ax = HPI[["USA", "SP500", "GDP"]].plot(ax=ax1)
HPI[["MORG", "UNEMPLOYMENT"]].plot(ax=ax2)
plt.show()
