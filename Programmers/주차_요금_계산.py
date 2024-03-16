import math

def minutes(date):
    h, m = map(int, date.split(':'))
    return h*60 + m

def solution(fees, records):
    answer = []
    dic = {}
    
    for i in records:
        time, num, idx = i.split(" ")
        
        num = int(num)
        
        if num in dic:
            dic[num].append([minutes(time), idx])
        else:
            dic[num] = [[minutes(time), idx]]
        
    item = list(dic.items())
    item.sort(key=lambda x : x[0])
    
    for i in item:
        t = 0
        
        for j in i[1]:
            if j[1] == "IN":
                t -= j[0]
            else:
                t += j[0]

        if i[1][-1][1] == "IN":
            t += minutes('23:59')
        
        if t <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((t-fees[0]) / fees[2]) * fees[3])        

    return answer