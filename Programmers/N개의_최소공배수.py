def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

def solution(arr):
    answer = arr[0]
    
    for i in arr:
        answer = lcm(i, answer)
            
    return answer

# math 모듈을 사용하면 더 간단하게 풀 수 있겠지만
# 최소공배수를 구하는 함수를 작성해서 풀어봤다.