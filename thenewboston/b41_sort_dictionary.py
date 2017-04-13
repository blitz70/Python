# data structure, dictionary sort

stocks = {
    'NAVER': 7688000,
    '바이오로그디바이스': 3900,
    '안랩': 111700,
    '삼성물산': 125000,
    '넥솔론': 60,
    '한국한공우주': 56900
}

print(stocks.keys())
print(stocks.values())
print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys()), reverse=True))
