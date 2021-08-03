n = 1640
count = 0
coin_number = [500, 100, 50, 10]

for coin in coin_number:
    count += n // coin
    n %= coin

print(count)