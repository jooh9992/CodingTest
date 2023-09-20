import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr_counter = Counter(arr)

answer = 0

for i in range(N):
    start = i +1
    end = N-1

    while start < end:
        value = arr[start] + arr[end] + arr[i]
        if value < 0:
            start += 1
        elif value == 0:
            if arr[start] == arr[end]:
                answer += end-start
            else:
                answer += arr_counter[arr[end]]
            start += 1
        else:
            end -= 1

print(answer)