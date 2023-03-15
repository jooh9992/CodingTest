from sys import stdin

n, k = map(int, stdin.readline().split())
coins = []
for i in range(n):
    v = int(stdin.readline())
    coins.append(v)
    
coins.reverse()
count = 0

for coin in coins:
    if coin <= k:
        count += k//coin
        k %= coin

print(count)