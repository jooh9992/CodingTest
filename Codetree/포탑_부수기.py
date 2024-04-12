from collections import deque

file = open("test.txt", "r")
input = file.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
turn = 0
vis = [[0] * m for _ in range(n)]
back_x = [[0] * m for _ in range(n)]
back_y = [[0] * m for _ in range(n)]
is_active = [[False] * m for _ in range(n)]
rec = [[0] * m for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dxs2, dys2 = [0, 0, 0, -1, -1, -1, 1, 1, 1], [0, -1, 1, 0, -1, 1, 0, -1, 1]

towers = [] #[행, 열, 공격력, 공격시점]

def init():
    global turn

    turn += 1
    for i in range(n):
        for j in range(m):
            vis[i][j] = False
            is_active[i][j] = False

# 공격자 및 공격 당할 타워 선정
def fighter():
    towers.sort(key=lambda x: (x[2], -x[3], -(x[0]+x[1]), -x[1]))

    weak_turret = towers[0]
    x = weak_turret[0]
    y = weak_turret[1]

    board[x][y] += n + m
    rec[x][y] = turn
    weak_turret[2] = board[x][y]
    weak_turret[3] = rec[x][y]
    is_active[x][y] = True

    towers[0] = weak_turret

# 레이저 공격
def laser_attack():
    weak_turret = towers[0]
    sx = weak_turret[0]
    sy = weak_turret[1]
    power = weak_turret[2]

    strong_turret = towers[-1]
    ex = strong_turret[0]
    ey = strong_turret[1]

    # bfs를 통해 최단경로를 관리
    q = deque()
    vis[sx][sy] = True
    q.append((sx, sy))

    # 가장 강한 포탑에게 도달 가능한지 여부를 can_attack에 관리
    can_attack = False

    while q:
        x, y = q.popleft()

        # 가장 강한 포탑에게 도달할 수 있다면
        # 바로 멈춤
        if x == ex and y == ey:
            can_attack = True
            break

        # 각각 우, 하, 좌, 상 순서대로 방문하며 방문 가능한 포탑들을 찾고
        # queue에 저장해줍니다.
        for dx, dy in zip(dxs, dys):
            nx = (x + dx + n) % n
            ny = (y + dy + m) % m

            # 이미 방문한 포탑이라면 넘어갑니다.
            if vis[nx][ny]:
                continue

            # 벽이라면 넘어갑니다.
            if board[nx][ny] == 0:
                continue

            vis[nx][ny] = True
            back_x[nx][ny] = x
            back_y[nx][ny] = y
            q.append((nx, ny))

    # 만약 도달 가능하다면 공격을 진행
    if can_attack:
        board[ex][ey] -= power
        if board[ex][ey] < 0:
            board[ex][ey] = 0
        is_active[ex][ey] = True

        cx = back_x[ex][ey]
        cy = back_y[ex][ey]

        while not (cx == sx and cy == sy):
            board[cx][cy] -= power // 2
            if board[cx][cy] < 0:
                board[cx][cy] = 0
            is_active[cx][cy] = True

            next_cx = back_x[cx][cy]
            next_cy = back_y[cx][cy]

            cx = next_cx
            cy = next_cy

    # 공격을 성공했는지 여부 반환
    return can_attack

# 폭탄 공격
def bomb():
    weak_turret = towers[0]
    sx = weak_turret[0]
    sy = weak_turret[1]
    power = weak_turret[2]

    strong_turret = towers[-1]
    ex = strong_turret[0]
    ey = strong_turret[1]

    for dx2, dy2 in zip(dxs2, dys2):
        nx = (ex + dx2 + n) % n
        ny = (ey + dy2 + m) % m

        if nx == sx and ny == sy:
            continue

        # 가장 강한 포탑일 경우 pow만큼의 공격을 진행
        if nx == ex and ny == ey:
            board[nx][ny] -= power
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            is_active[nx][ny] = True
        # 그 외의 경우 pow // 2만큼의 공격을 진행
        else:
            board[nx][ny] -= power // 2
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            is_active[nx][ny] = True


# 공격에 관여하지 않은 모든 살아있는 포탑의 힘을 1 증가
def reserve():
    for i in range(n):
        for j in range(m):
            if is_active[i][j]:
                continue
            if board[i][j] == 0:
                continue
            board[i][j] += 1

for _ in range(k):
    # 살아 있는 포탑 정리
    towers = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                towers.append([i, j, board[i][j], rec[i][j]])

    if len(towers)<= 1:
        break

    init()

    fighter()

    is_suc = laser_attack()

    if not is_suc:
        bomb()

    reserve()

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, board[i][j])

print(answer)