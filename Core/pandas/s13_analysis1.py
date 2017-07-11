import pandas as pd
import quandl


def state_list():
    _state_list = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
    return _state_list[0][0][1:]


def hpi_states_data():
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


def hpi_usa_data():
    df = quandl.get("FMAC/HPI_USA", api_key=key)
    df.rename(columns={"Value": "USA"}, inplace=True)
    return df


def morg_usa_data():
    df = quandl.get("FMAC/30US", api_key=key)
    df.rename(columns={"Value": "MORG"}, inplace=True)
    return df


def modify_data():
    for data in hpi_states:
        hpi_states[data] = (hpi_states[data] - hpi_states[data][0]) / hpi_states[data][0] * 100
    hpi_usa["USA"] = (hpi_usa["USA"] - hpi_usa["USA"][0]) / hpi_usa["USA"][0] * 100
    global morg_usa
    morg_usa = morg_usa.resample("M").mean()
    morg_usa = morg_usa[:]["1975-01-31":]
    morg_usa["MORG"] = (morg_usa["MORG"] - morg_usa["MORG"][0]) / morg_usa["MORG"][0] *100


key = open("apikey.txt", "r").read()

# print("make data")
# hpi_states = hpi_states_data()
# hpi_usa = hpi_usa_data()
# morg_usa = morg_usa_data()
#
# print("save data")
# hpi_states.to_pickle("hpi_states.pickle")
# hpi_usa.to_pickle("hpi_usa.pickle")
# morg_usa.to_pickle("morg_usa.pickle")

print("load data")
hpi_states = pd.read_pickle("hpi_states.pickle")
hpi_usa = pd.read_pickle("hpi_usa.pickle")
morg_usa = pd.read_pickle("morg_usa.pickle")

modify_data()

hpi_states_usa = hpi_states.join(hpi_usa)
hpi_states_morg = hpi_states.join(morg_usa)

# state = []
# mean = []
# for data in hpi_states:
#     state.append(data)
#     mean.append(hpi_states.corr().describe()[data]["mean"])
# stats = {"states": state, "mean": mean}
# stats = pd.DataFrame(stats)
# stats.set_index("states", inplace=True)

print("STATES")
hpi_states_desc = hpi_states.corr().describe()
print(hpi_states_desc)
print("USA")
hpi_states_usa_desc = hpi_states_usa.corr()[["USA"]].describe()
print(hpi_states_usa_desc)
print("MORG")
hpi_states_morg_desc = hpi_states_morg.corr()[["MORG"]].describe()
print(hpi_states_morg_desc)
print("Summary")
print(hpi_states_usa_desc.join(hpi_states_morg_desc))


