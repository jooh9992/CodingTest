import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = [0,0]

def recursive(x, y, n):
    global result

    num = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if (board[i][j] != num):
                for k in range(2):
                    for l in range(2):
                        recursive(x + k * n // 2, y + l * n // 2, n // 2)
                return 

    if num == 0:
        result[0] += 1
    else:
        result[1] += 1


recursive(0, 0, N)
[print(r) for r in result]