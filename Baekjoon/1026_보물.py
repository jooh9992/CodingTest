from sys import stdin

n = int(stdin.readline())

A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A.sort()
answer = 0

for i in range(n):
    a = A[i]
    b = B.pop(B.index(max(B)))

    answer += a *b

print(answer)