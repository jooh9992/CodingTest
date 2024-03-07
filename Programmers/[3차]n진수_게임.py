# n진법에서 10을 넘어가는 숫자를 영어로 치환하는 함수
def convert_to_alpha(num):
    if num < 10:
        return str(num)
    else:
        return chr(ord('A') + num - 10)

# n진법 구하는 함수
def convert(k, j):
    base = ''
    
    while k > 0:
        k, m = divmod(k, j) 
        base += convert_to_alpha(m)
        
    return base[::-1]

# 위치에 있는 값을 출력        
def solution(n, t, m, p):
    answer = ''
    li = '0'
    
    for i in range((t*m)):
        li += convert(i, n)
        
    for i in range((t*m)):
        if i % m == (p-1):
            answer += li[i]
    
    return answer

# ------------------

# 위와 같은 방법으로 함수를 2개를 생성해서 풀었으나
# 두 개의 함수를 한번에 아래와 같이 구현할 수 있다.

def convert(m,n):
    total = "0123456789ABCDEF"
    i,j = divmod(m,n)
    if i ==0:
        return total[j]
    else : 
        return convert(i,n)+total[j]

# 재귀함수를 사용해서 한자리이면 바로 total에서 값을 출력하고
# 그 이상의 자리수라면 재귀함수로 다시 실행한 후 값을 출력함