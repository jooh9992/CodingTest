from itertools import permutations

#완전탐색 문제이고 dungeons가 8까지 밖에 없기 때문에
#순열을 사용해서 전체를 탐색해도 괜찮
def solution(k, dungeons):
    answer = []
    dun = []
    
    #모든 경우의 수를 순열로 만들어줌
    for i in permutations(dungeons, len(dungeons)):
        dun.append(i)
    
    #순회하면서 지금 피로도와 최소 필요 필요도를 비교하여 계산
    for i in dun:
        power = k
        cnt = 0
        for j in i:
            if j[0] <= power:
                power -= j[1]
                cnt +=1
                
        answer.append(cnt)
        
    return max(answer)