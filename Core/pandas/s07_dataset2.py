import pandas as pd
import quandl
import pickle
import time
import simplejson


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
        # print(state_df.head())
    # print(states_df.head())
    return states_df


def save_data(data):  # pickle
    with open("state_list.pickle", "wb") as f:
        pickle.dump(data, f)


def load_data():
    with open("state_list.pickle", "rb") as f:
        return pickle.load(f)

# data analysis : do housing price index(HPI) behave similarly?

key = open("apikey.txt", "r").read()

t = time.process_time()
data = make_data()
print("make data : ", time.process_time() - t)

t = time.process_time()
save_data(data)
HPI_data = load_data()
print(HPI_data.head())
print("pickle : ", time.process_time() - t)

t = time.process_time()
data.to_pickle("state_list.p_pickle")
HPI_data2 = pd.read_pickle("state_list.p_pickle")
print(HPI_data2.head())
print("P pickle : ", time.process_time() - t)

t = time.process_time()
data.to_json("state_list.json")
HPI_data3 = pd.read_json("state_list.json")
print(HPI_data3.head())
print("json : ", time.process_time() - t)

# t = time.process_time()
# with open("state_list.sjson", "w") as f:
#     simplejson.dump(data, f)
# with open("state_list.sjson", "r") as f:
#     HPI_data4 = simplejson.load(f)
#     print(HPI_data4.head())
# print("sjson : ", time.process_time() - t)

