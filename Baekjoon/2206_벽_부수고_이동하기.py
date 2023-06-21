import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# 3차원 리스트(행, 열, 벽깬여부) 생성
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

#상하좌우 이동 표시
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    # (0, 0) 출발, 벽 안부순 상태에서 시작
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        r, c, wall = q.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][wall]

        for i in range(4):
            #상하좌우를 이동하면서 새로운 위치를 계산
            nr = r + dx[i]
            nc = c + dy[i]

            # 맵의 범위 안에 있고, 한 번도 방문하지 않았으면 검사
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][wall] == 0:
                # 벽이 아니라면 이동하고, 이전경로의 길에 +1을 해서 visited 배열에 저장
                if graph[nr][nc] == 0:
                    q.append((nr, nc, wall))
                    visited[nr][nc][wall] = visited[r][c][wall] + 1
                
                # 벽을 아직 부수지 않은 상태고, 새로운 위치가 벽인 경우
                if wall == 0 and graph[nr][nc] == 1:
                    # 벽을 부순 상태를 1로 표현
                    q.append((nr, nc, 1))
                    # 벽 부순 상태의 visited[nr][nc][1]에 이전경로 + 1 저장
                    visited[nr][nc][1] = visited[r][c][wall] + 1

    #BFS 탐색이 끝나도 도착점에 도달하지 못한 경우, -1을 반환함
    return -1

print(bfs())