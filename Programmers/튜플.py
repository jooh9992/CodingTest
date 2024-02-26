def solution(s):
    answer = []
    li = []
    s = s[2:-2]
    for i in s.split("},{"):
        li.append(i)
    
    li.sort(key=lambda x : len(x))
    
    for i in li:
        for j in i.split(","):
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer

#split for문 수정
def solution(s):
    answer = []
    li = s[2:-2].split("},{")
    li.sort(key=lambda x : len(x))
    
    for i in li:
        for j in i.split(","):
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer