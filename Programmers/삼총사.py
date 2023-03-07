import itertools

def solution(number):
    answer = 0
    num = itertools.combinations(number,3)
    for n in num:
        if sum(n) ==0:
            answer+= 1
    
    return answer