prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
total = 0
for k in stock.keys():
    print(k, stock[k])
    print("price:",prices[k])
    a = stock[k] * prices[k]
    print("Each: ",a)
    print()
    total += a
print("Total ",total)
