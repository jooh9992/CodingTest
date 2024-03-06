# n진수 변환 함수
def convert(n, q):
    base = ' '

    while n > 0:
        n, mod = divmod(n, q)
        base += str(mod)

    return base[::-1]

# 소수 판별 함수
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2) +1)):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = convert(n, k)
    nums = num.split("0")

    for n in nums:
        if n and isPrime(int(n)):
            answer += 1
        
    return answer
