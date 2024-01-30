#DP 문제
#만약 N이 5이면
#dp[1] = {5}
#dp[2] = {55, 5+5, 5-5, 5*5, 5/5}
#dp[3] = {555, 55+5, 55-5, 55*5, 55/5..}
#위의 식으로 보면 555 , (dp[1] 연산 dp[2]) , (dp[2] 연산 dp[1])이 되는 것을 볼 수 있음
#따라서, N을 n개 사용해서 나타낼 수 있는 수는
# (N을 i개 사용해서 나타낼수 있는 수) 연산 (N을 n-i개 사용해서 나타낼수 있는 수) (1<=i<n)
def solution(N, number):
    dp = [set() for i in range(9)] # 사용횟수에 따라 가능한 숫자를 담을 리스트
    for i in range(1, 9): # 1~8
        dp[i].add(int(str(N)*i)) # 단순히 이어붙인 숫자
        for j in range(i):
            for first in dp[j]:
                for second in dp[i-j]:
                    dp[i].add(first + second)
                    dp[i].add(first - second)
                    dp[i].add(first * second)
                    if second != 0 :
                        dp[i].add(first // second)
        if number in dp[i]:
            return i
    return -1