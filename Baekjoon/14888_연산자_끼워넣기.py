import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maxnum = -1e9
minnum = 1e9

#백트래킹
def dfs(depth, sum, add, sub, mul, div):
    global maxnum, minnum

    if depth == N:
        maxnum = max(sum, maxnum)
        minnum = min(sum, minnum)
        return
    
    if add:
        dfs(depth +1, sum + num[depth], add-1, sub, mul, div)
    if sub:
        dfs(depth +1, sum - num[depth], add, sub-1, mul, div)
    if mul:
        dfs(depth +1, sum * num[depth], add, sub, mul-1, div)
    if div:
        dfs(depth +1, int(sum / num[depth]), add, sub, mul, div-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maxnum)
print(minnum)