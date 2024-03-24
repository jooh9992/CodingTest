def solution(record):
    answer = []
    names = {}
    
    for i in record:
        if len(i.split()) == 3:
            re, ids, name = i.split()
            names[ids] = name
    
    for i in record:
        if len(i.split()) == 3:
            re, ids, name = i.split()
            if re =="Enter":
                answer.append(f'{names[ids]}님이 들어왔습니다.')
        else:
            re, ids = i.split()
            answer.append(f'{names[ids]}님이 나갔습니다.')
    
    
    return answer

# 코드 줄이기

def solution(record):
    answer = []
    names = {}
    
    for i in record:
        ii = i.split()
        if ii[0] != "Leave":
            names[ii[1]] = ii[2]
    
    for i in record:
        ii = i.split()
        
        if ii[0] == "Enter":
            answer.append(f'{names[ii[1]]}님이 들어왔습니다.')
        elif ii[0] == "Leave":
            answer.append(f'{names[ii[1]]}님이 나갔습니다.')
    
    return answer