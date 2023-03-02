def solution(n):
    x = n ** (1/2) 
    if x % 1 == 0: #루트를 해서 정수로 떨어지면 제곱근!
        return (x + 1) ** 2
    return -1