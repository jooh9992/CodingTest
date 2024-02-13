def solution(s):
    l = []
    
    for i in s:
        l.append(i)
        if len(l) > 1 and l[-1] == l[-2]:
            l.pop()
            l.pop()
            
    if len(l) == 0:
        return 1
    else:
        return 0