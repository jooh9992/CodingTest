import sys
input = sys.stdin.readline

n = int(input())

s = [list(map(int, input().split())) for i in range(n)]

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if s[i][0] + i <= n:
        dp[i] = max(s[i][1] + dp[i + s[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])