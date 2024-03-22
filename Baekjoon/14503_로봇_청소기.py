import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

#북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited[r][c] = 1
answer = 1

while True:
    #청소 유무
    flag = 0
    
    #주변 4칸을 탐색
    for _ in range(4):
        d = (d+3) % 4 # 서, 남, 동, 북
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                answer += 1
                r = nr
                c = nc
                flag = 1
                break
    
    #청소되지 않은 빈 칸이 없는 경우
    if flag == 0:
        #후진한 칸이 벽이면 작동을 멈춤
        if room[r-dr[d]][c-dc[d]] == 1:
            print(answer)
            break
        else:
            r, c = r- dr[d], c-dc[d]