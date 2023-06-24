import sys
from collections import deque

imput = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dir = ((0, 1), (0, -1), (1, 0), (-1, 0))

def condition(ni, nj):
    return ni < 0 or ni >= n or nj < 0 or nj >= n or visited[ni][nj]

def marking(y, x, mark):
    q = deque()
    q.append((y, x))
    graph[y][x] = mark
    visited[y][x] = True
    while q:
        i, j = q.popleft()
        for dy, dx in dir:
            ni, nj = i + dy, j + dx
            if condition(ni, nj) or not graph[ni][nj]:   continue
            graph[ni][nj] = mark
            visited[ni][nj] = True
            q.append((ni, nj))

def getDist(y, x, now):
    q = deque()
    q.append((y, x, 0))
    while q:
        i, j, cnt = q.popleft()
        if graph[i][j] != 0 and graph[i][j] != now:
            return cnt
        for dy, dx in dir:
            ni, nj = i + dy, j + dx
            if condition(ni, nj) or graph[ni][nj] == now:   continue
            visited[ni][nj] = True
            q.append((ni, nj, cnt + 1))
    return 2000
            

mark = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            marking(i, j, mark)
            mark += 1

ans = 2000
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            visited = [[False] * n for _ in range(n)]
            ans = min(ans, getDist(i, j, graph[i][j]))
        
print(ans - 1)