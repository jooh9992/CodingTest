def solution(bandage, health, attacks):
    time = attacks[-1][0]
    answer = health
    attack_dict = {}
    for i in attacks:
        attack_dict[i[0]]=i[1]
        
    t = 0
    sec = 0
    
    while t <= time:
        if t in attack_dict:
            answer -= attack_dict[t]
            sec = 0
            
            if answer <= 0:
                return -1
        
        else:
            sec += 1
            if sec < bandage[0]:
                answer += bandage[1]
                if answer > health:
                    answer = health
                    
            else:
                answer = answer + bandage[1] + bandage[2]
                if answer > health:
                    answer = health
                sec = 0
        t += 1
    return answer