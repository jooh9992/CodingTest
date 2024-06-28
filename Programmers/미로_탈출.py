from collections import deque

def bfs(s, e, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]

    q = deque()
    flag = False

    for i in range(n):
        for j in range(m):
            if maps[i][j] == s:
                q.append((i, j, 0))
                visited[i][j] = True
                flag = True
                break
        if flag:
            break
    
    while q:
        y, x, cnt = q.popleft()

        if maps[y][x] == e:
            return cnt
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X':
                if not visited[ny][nx]:
                    q.append((ny, nx, cnt+1))
                    visited[ny][nx] = True
    
    return -1


def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)

    if path1 != -1 and path2 != -1:
        return path1 + path2
    
    return -1