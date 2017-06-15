import pandas as pd
import quandl

key = open("apikey.txt", "r").read()

df = quandl.get("FMAC/HPI_TX", api_key=key)

print(df.head())


