import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = [0,0,0]

def recursive(x, y, n):
    global result

    num = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if (board[i][j] != num):
                for k in range(3):
                    for l in range(3):
                        recursive(x + k * n // 3, y + l * n // 3, n // 3)
                return 

    if num == -1:
        result[0] += 1
    elif num == 0:
        result[1] += 1
    else:
        result[2] += 1


recursive(0, 0, N)
[print(r) for r in result]