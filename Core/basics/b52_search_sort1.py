# data structure : searching and sorting, heapq, complex list of dictionaries

import heapq

# search 3 largest items in list
grades = [32, 44, 76, 89, 67, 26, 92, 54]
top_three = heapq.nlargest(3, grades)
print(top_three)

# search 2 smallest items in complex list
stocks = [
    {'ticker': 'AAPL', 'price': 291},
    {'ticker': 'GOOG', 'price': 800},
    {'ticker': 'F', 'price': 54},
    {'ticker': 'MSFT', 'price': 313}
]
bottom_two = heapq.nsmallest(2, stocks, key=lambda x: x['price'])
print(bottom_two)
