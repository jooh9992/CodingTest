import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
deque = deque([i for i in range(1, N+1)])
arr = list(map(int, input().split()))
count = 0

for i in arr:
    while True:
        if deque[0] == i:
            deque.popleft()
            break
        else:
            if deque.index(i) <= len(deque)/2:
                deque.rotate(-1)
                count += 1
            else:
                deque.rotate(1)
                count += 1

print(count)