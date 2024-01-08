def solution(s):
    answer = False
    p = []
    
    for i in s:
        if i == ")":
            if len(p) != 0 and p[-1] == "(":
                p.pop()
            else:
                p.append(i)
        else:
            p.append(i)
    
    if len(p) == 0:
        answer = True
        
    return answer