def solution(n):
    answer = 0
    a = 1
    b = 2

    for i in range(3, n+1):
        answer = a+b
        a = b
        b = answer
        
    return answer % 1000000007