# 인덱스의 몫과 나머지로 배열의 행과 열을 알 수 있었다.
# 그 중 큰 값에 1을 더해 값을 찾았다.
def solution(n, left, right):
    answer = []
    
    for i in range(left, right +1):
        answer.append(max(i//n, i%n) +1)

    return answer