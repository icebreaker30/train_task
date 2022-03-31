
prices = [7,1,5,3,6,4]
a = min(prices)

prices = prices[prices.index(a):]

b = max(prices)
if prices.index(a) != prices.index(b):
    print (b - a)
else:
    print(0)