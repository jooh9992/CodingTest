import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]

result = ""

def recursive(x, y, n):
    global result

    num = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != board[i][j]:
                result += "("
                recursive(x, y, n//2) #1사분면
                recursive(x, y+n//2, n//2) #2사분면
                recursive(x+n//2, y, n//2) #3사분면
                recursive(x+n//2, y+n//2, n//2) #4사분면
                result += ")"
                return

    if num == 0:
        result += '0'
    else:
        result += "1"


recursive(0, 0, N)
print(result)