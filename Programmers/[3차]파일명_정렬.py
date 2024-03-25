def solution(files):
    answer = []
    head, number, tail = "", "", ""
    
#HEAD, NUMBER, TAIL 파싱
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                
                answer.append([head, number, tail])
                head, number, tail = "", "", ""
                break
#정렬           
    answer = sorted(answer, key= lambda x:(x[0].lower(), int(x[1])))
    
    return ["".join(i) for i in answer]


# 정규식을 이용한 풀이
import re

def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]
