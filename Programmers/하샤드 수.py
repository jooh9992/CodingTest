def solution(x):
    answer = True
    
    if x > 1:
        s = sum([int(i) for i in str(x)])
        if x %s !=0:
            answer = False
    
    return answer