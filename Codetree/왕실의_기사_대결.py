from collections import deque

# 전역 변수들을 정의
MAX_N = 31 # 최대 기사 수
MAX_L = 41 # 최대 체스판 크기
info = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)] # 체스판
bef_k = [0 for _ in range(MAX_N)] # 기사들의 초기 체력
r = [0 for _ in range(MAX_N)] # 처음 기사 위치 행
c = [0 for _ in range(MAX_N)] # 처음 기사 위치 열
h = [0 for _ in range(MAX_N)] # 기사의 세로 h
w = [0 for _ in range(MAX_N)] # 기사의 가로 w
k = [0 for _ in range(MAX_N)] # 기사의 체력
nr = [0 for _ in range(MAX_N)] # 움직일 위치 행
nc = [0 for _ in range(MAX_N)] # 움직일 위치 열
dmg = [0 for _ in range(MAX_N)] # 기사가 받은 데미지
is_moved = [False for _ in range(MAX_N)] # 움직임 확인

l, n, q = map(int, input().split())
for i in range(1, l + 1):
    info[i][1:] = map(int, input().split()) # 체스판 정보 입력
for i in range(1, n + 1):
    r[i], c[i], h[i], w[i], k[i] = map(int, input().split())
    bef_k[i] = k[i]

#위, 오, 아, 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 움직임을 시도하는 함수
def try_movement(idx, dir):
    q = deque()

    # 초기화 작업
    for i in range(1, n + 1):
        dmg[i] = 0
        is_moved[i] = False
        nr[i] = r[i]
        nc[i] = c[i]

    q.append(idx)
    is_moved[idx] = True

    while q:
        x = q.popleft()

        nr[x] += dx[dir]
        nc[x] += dy[dir]

        # 경계를 벗어나는지 체크
        if nr[x] < 1 or nc[x] < 1 or nr[x] + h[x] - 1 > l or nc[x] + w[x] - 1 > l:
            return False

        # 대상 조각이 다른 조각이나 장애물과 충돌하는지 검사
        for i in range(nr[x], nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if info[i][j] == 1:
                    dmg[x] += 1
                if info[i][j] == 2:
                    return False

        # 다른 조각과 충돌하는 경우, 해당 조각도 같이 이동
        for i in range(1, n + 1):
            if is_moved[i] or k[i] <= 0:
                continue
            if r[i] > nr[x] + h[x] - 1 or nr[x] > r[i] + h[i] - 1:
                continue
            if c[i] > nc[x] + w[x] - 1 or nc[x] > c[i] + w[i] - 1:
                continue

            is_moved[i] = True
            q.append(i)

    dmg[idx] = 0
    return True


# 특정 조각을 지정된 방향으로 이동시키는 함수
def move_piece(idx, move_dir):
    if k[idx] <= 0:
        return

    # 이동이 가능한 경우, 실제 위치와 체력을 업데이트
    if try_movement(idx, move_dir):
        for i in range(1, n + 1):
            r[i] = nr[i]
            c[i] = nc[i]
            k[i] -= dmg[i]


# 왕의 명령 실행
for _ in range(q):
    idx, d = map(int, input().split())
    move_piece(idx, d)

# 결과를 계산하고 출력
ans = sum([bef_k[i] - k[i] for i in range(1, n + 1) if k[i] > 0])
print(ans)