def solution(keymap, targets):
    answer = []
    dic = {}
    
    for i in keymap:
        for j in i:
            if j not in dic:
                dic[j] = i.index(j) + 1
            else:
                dic[j] = min(dic[j], i.index(j) + 1)
            
    for i in targets:
        count = 0
        for j in i:
            if j in dic:
                count += dic[j]
            elif j not in dic:
                count = -1
                break
        answer.append(count) 
    
    return answer