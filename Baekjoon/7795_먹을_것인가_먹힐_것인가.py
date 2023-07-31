import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    cnt = 0
    n, m = map(int, input().split())
    n_num = sorted(list(map(int, input().split())))
    m_num = sorted(list(map(int, input().split())))
    ans = 0
    
    for i in range(n):
        while True:
            if cnt == m or n_num[i] <= m_num[cnt]:
                ans += cnt
                break
            else:
                cnt += 1

    print(ans)