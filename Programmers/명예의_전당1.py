def solution(k, score):
    answer = []
    
    for i in range(0, len(score)):
        if i < k:
            a = score[:i+1]
            a.sort()
            answer.append(a[0])
        else:
            a = score[:i+1]
            a.sort(reverse=True)
            answer.append(a[k-1]) 

    return answer