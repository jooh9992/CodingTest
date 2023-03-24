import sys
from collections import deque

t = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny <m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a]= 1

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
