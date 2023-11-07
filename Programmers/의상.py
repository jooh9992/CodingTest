def solution(clothes):
    answer = 1
    
    dic = {c[1] : [] for c in clothes}
    
    for i in clothes:
        dic[i[1]].append(i[0])
    
    for j in dic.keys():
        n = len(dic[j])
        answer *= (n+1)
    
    return answer-1