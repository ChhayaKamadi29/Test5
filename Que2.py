#2. A teacher came to class with a large box tokhat has several coins. Each coin has a number printed on it. Before coming to class, she ensured that All the numbers occur an Even number of times. However, while coming to the class, one coin fell down and got lost. She wants to find out the number on the missing coin

total_coins = 8
coins = [5, 7, 2, 7, 5, 2, 5]

freq = {}
for coin in coins:
    if coin in freq:
        freq[coin] = freq[coin] + 1
    else:
        freq[coin] = 1

for coin in freq:
    if freq[coin] % 2 != 0:
        print(coin)
        break