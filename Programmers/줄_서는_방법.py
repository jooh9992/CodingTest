import math

def solution(n, k):
    stack = [i for i in range(1, n + 1)]
    answer = []
    k = k-1

    while stack:
        a = k // math.factorial(n - 1)
        answer.append(stack[a])
        del stack[a]

        k = k % math.factorial(n - 1)
        n -= 1
        
    return answer