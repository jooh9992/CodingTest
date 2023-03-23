# dfs 방법
from sys import stdin

def dfs(x, y):
    stack = [(x, y)]
    cnt = 0
    while stack:
        x, y = stack.pop()
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if visited[x][y] or graph[x][y] == 0:
            continue
        visited[x][y] = True
        cnt += 1
        stack.append((x-1, y))
        stack.append((x, y-1))
        stack.append((x+1, y))
        stack.append((x, y+1))
    return cnt

n, m = map(int, stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))

visited = [[False] * m for _ in range(n)]
result = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            size = dfs(i, j)
            result += 1
            max_size = max(max_size, size)

print(result)
print(max_size)

# bfs 방법
from collections import deque
from sys import stdin

def bfs(x, y):
    graph[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    width = 1
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = 0
                width += 1
    return width


n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

count = 0
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count += 1
            answer = max(bfs(i, j), answer)

print(count)
print(answer)