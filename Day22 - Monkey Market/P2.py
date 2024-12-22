with open('input.txt', 'r', encoding="utf-8") as f:
    initial, sales, highest = [], {}, 0
    for line in f.readlines():
        initial.append(int(line.strip()))

mix = lambda a, b: a ^ b
prune = lambda a: a % 16777216

for secret in initial:
    prices = []
    sales_now = {}
    for _ in range(2000):
        secret = prune(mix(secret * 64, secret))
        secret = prune(mix(secret // 32, secret))
        secret = prune(mix(secret * 2048, secret))
        prices.append(int(str(secret)[-1]))
        if len(prices) >= 5:
            if (prices[-4] - prices[-5], prices[-3] - prices[-4], prices[-2] - prices[-3], prices[-1] - prices[-2]) not in sales:
                sales[(prices[-4] - prices[-5], prices[-3] - prices[-4], prices[-2] - prices[-3], prices[-1] - prices[-2])] = prices[-1]
                sales_now[(prices[-4] - prices[-5], prices[-3] - prices[-4], prices[-2] - prices[-3], prices[-1] - prices[-2])] = prices[-1]
            elif (prices[-4] - prices[-5], prices[-3] - prices[-4], prices[-2] - prices[-3], prices[-1] - prices[-2]) not in sales_now:
                sales[(prices[-4] - prices[-5], prices[-3] - prices[-4], prices[-2] - prices[-3], prices[-1] - prices[-2])] += prices[-1]
                sales_now[(prices[-4] - prices[-5], prices[-3] - prices[-4], prices[-2] - prices[-3], prices[-1] - prices[-2])] = prices[-1]

for key in sales:
    if sales[key] > highest:
        highest = sales[key]
print(highest)
