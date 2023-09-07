def solution(N, stages):
    dic = {}
    sum = len(stages)
    
    for i in range(1, N+1):
        if sum != 0:
            count = stages.count(i)
            dic[i] = count / sum
            sum -= count
        else:
            dic[i] = 0

    return sorted(dic,key=lambda x:dic[x], reverse=True)