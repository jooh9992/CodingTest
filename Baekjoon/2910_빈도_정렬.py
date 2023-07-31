import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = {}

num = list(map(int, input().split()))

for i in num:
    if i in arr:
        arr[i] += 1
    else:
        arr[i] = 1

arr = sorted(arr.items(), key=lambda x: x[1], reverse=True)

for i in arr:
    for j in range(i[1]):
        print(i[0], end=' ')

#Counter 사용 방법
from collections import Counter

x = Counter(num).most_common()

for a,b in x:
    for i in range(b):
        print(a, end=' ')