def solution(d, budget):
    answer = 0
    result=0
    count=0
    if budget >= sum(d):
        answer= len(d)
    
    d.sort()
    
    for i in d:
        result += i
        count += 1
        if budget >=result:
            answer = count
    return answer