import sys
input = sys.stdin.readline

def result(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (result(a,b//2,c)**2)%c
    else:
        return ((result(a,b//2,c)**2)*a)%c

A, B, C = map(int, input().split())
print(result(A, B, C))

#분할 정복 알고리즘 사용 원리
#예를 들어, a^b를 계산할 때 b가 짝수인 경우, (a^(b/2))^2의 값을 계산하고, b가 홀수인 경우, ((a^(b/2))^2) * a의 값을 계산