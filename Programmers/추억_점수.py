def solution(name, yearning, photo):
    answer = []
    
    name_score = dict(zip(name, yearning))
    
    for people in photo:
        sum = 0
        
        for name in people:
            sum+= name_score.get(name, 0)
            
        answer.append(sum)
    
    return answer