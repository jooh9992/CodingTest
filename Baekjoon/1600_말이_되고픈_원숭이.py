import sys
from collections import deque
input = sys.stdin.readline

k = int(input()) #특수 이동을 사용할 수 있는 최대 개수
m , n = map(int, input().split()) #테이블의 행과 열
table = [list(map(int, input().split())) for _ in range(n)] #테이블 값

# dx, dy : 일반적인 동서남북 4방향
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# hx, hy : 특수 이동인 8방향
hx = [-1,-2,-1,-2,1,2,1,2]
hy = [-2,-1,2,1,-2,-1,2,1]

# 특수 이동 횟수를 고려하여 방문 여부를 저장하는 배열
check = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

# go : (a,b)에서 시작하여 특수이동, 일반이동을 모두 고려했을 때 도착점까지의 최소 동작 횟수를 계산하는 함수
def bfs(a,b):
    q = deque()
    q.append((a,b,0,0)) #해당 위치를 방문 했음을 표시
    # 처음에는 특수 이동을 쓰지 않았으므로 [a][b][0]이다
    check[a][b][0] = True
    while q:
        x,y,skill, cnt = q.popleft()
        # x, y : 현재 x좌표, y좌표, skill : 현재 특수 이동을 한 횟수, cnt : 그때의 동작 횟수
        
        # 도착했으면 cnt 반환하고 함수 종료
        if x == n - 1 and y == m - 1:
            return cnt
            
        # 일반적인 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] #현재위치에서 동서남북 방향으로 새로운 위치 계산
            if 0 <= nx < n and 0 <= ny < m: #새로운 위치가 범위내에 있을 때
                if check[nx][ny][skill] == False: #방문하지 않은 위치일 때
                    if table[nx][ny] == 0: #이동가능한 경우일 때
                        check[nx][ny][skill] = True #해당 위치를 방문했음(True)로 표시
                        q.append((nx, ny, skill, cnt + 1)) # 특수 이동을 쓰지 않았으므로 skill은 증가시키지 않고 큐에 추가

        # 특수 이동이 가능한 경우
        if skill < k:
            # 특수 이동 8방향 탐색
            for i in range(8):
                nx, ny = x + hx[i], y + hy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if check[nx][ny][skill + 1] == False: #특수이동횟수+1을 방문하지 않은 위치일 때
                        if table[nx][ny] == 0:
                            check[nx][ny][skill + 1] = True
                            # 다음 이동을 위해 특수 이동을 한번 썼기 때문에 skill을 1증가 시키고 큐에 추가
                            q.append((nx,ny,skill+1,cnt + 1))
    
    # 불가능한 경우 -1 리턴
    return -1

# 정답 출력
print(bfs(0,0))