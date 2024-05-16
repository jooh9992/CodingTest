from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, i, j, n, m, visited):
    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    day = int(maps[i][j])
    
    while q:
        x, y = q.popleft()
        
        for p in range(4):
            nx, ny = x+dx[p], y+dy[p]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                q.append((nx, ny))
                day += int(maps[nx][ny])
                visited[nx][ny] = 1
    return day
        

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited =[[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(bfs(maps, i, j, n, m, visited))
    
    if answer:
        return sorted(answer)
    else:
        return [-1]