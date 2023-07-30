import sys
input = sys.stdin.readline

n, *arr = input().split()
res = []
while len(arr) <int(n):
    arr.extend(input().split())

for i in arr:
    a = "".join(reversed(i)).lstrip("0")
    res.append(int(a))

res.sort()

for i in res:
    print(i)