from collections import deque

def solution(maps):
    #맵의 크기 저장
    n, m = len(maps), len(maps[0])

    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #BFS를 위한 큐를 선언하고 시작지점을 큐에 추가
    queue = deque()
    queue.append((0,0))

    while queue:
        #현재 위치를 가져옴
        x, y = queue.popleft()

        #상하좌우 이동을 반복
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #맵을 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽이거나 이미 방문한 지점이면 무시
            if maps[nx][ny] > 1 or maps[nx][ny] == 0:
                continue
            #시작 지점이면 무시
            if nx == 0 and ny == 0:
                continue
            
            #새로운 좌표를 큐에 추가
            queue.append((nx, ny))
            #새로운 좌표까지의 최단 경로의 길이를 현재까지의 최단 경로의 길이에 더함
            maps[nx][ny] += maps[x][y]

    #목적지에 도달했을 때의 최단 경로의 길이 반환, 도달할 수 없으면 -1 반환
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else:
        return -1