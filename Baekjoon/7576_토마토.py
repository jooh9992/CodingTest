import sys
from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] +1
                queue.append([nx, ny])

m, n = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque([])
dx = [1,-1,0,0]
dy = [0,0,-1,1]
result = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

bfs()

for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result -1)