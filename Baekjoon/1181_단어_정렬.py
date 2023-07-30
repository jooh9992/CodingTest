import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(input().strip())

res = list(set(arr))

res.sort(key=lambda x: (len(x), x))

for i in res:
    print(i)