def solution(id_list, report, k):
    dic = {}
    di = {}
    report = set(report)
    answer = []
    result = []
    
    for i in report:
        a, b = i.split(" ")
        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1
    
    for i in dic.keys():
        if dic[i] >= k:
            answer.append(i)
            
    for i in report:
        a, b = i.split(" ")
        if b in answer:
            if a in di:
                di[a] += 1
            else:
                di[a] = 1 
                
    for i in id_list:
        if i in di.keys():
            result.append(di[i])
        else:
            result.append(0)
    
    return result

#코드 리팩토링

def solution(id_list, report, k):
    report = set(report)
    answer = [0] * len(id_list)
    dic = {id: [] for id in id_list}
    
    for i in report:
        i = i.split()
        dic[i[1]].append(i[0])
    
    for key, value in dic.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1
    
    return answer