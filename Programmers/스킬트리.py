def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    li = ""
    
    for i in skill_trees:
        for j in i:
            if j in skill_list:
                li += j
        
        if skill.find(li) == 0:
            answer += 1
        li = ""
            
    return answer

    