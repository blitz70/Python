import pandas as pd
import quandl

# data analysis : do housing price index(HPI) behave similarly?

key = open("apikey.txt", "r").read()

df = quandl.get("FMAC/HPI_TX", api_key=key)
print(df.head())

# get quandl code for us states
us_states = pd.read_html("https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations")
us_states_quandl = []
for item in us_states[0][3]:
    if type(item) == str and len(item) == 2:
        us_states_quandl.append("".join(["FMAC/HPI_", item]))
[print(item) for item in us_states_quandl]
print(len(us_states_quandl))
