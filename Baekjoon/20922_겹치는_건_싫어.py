import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
start, end, count = 0, 0, defaultdict(int)

while end < N:
    if count[arr[end]] < K:
        count[arr[end]] += 1
        end += 1
    else:
        count[arr[start]] -= 1
        start += 1
    answer = max(answer, end-start)
print(answer)