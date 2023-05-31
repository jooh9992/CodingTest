import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

for i in range(N):
    queue.append(i+1)

# queue = deque([_ for _ in range(1, N+1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])