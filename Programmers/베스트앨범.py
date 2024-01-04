def solution(genres, plays):
    answer = []
    
    total={} #장르별 총 재생 횟수
    gen_dic={} #장르별 [재생 횟수 & 고유 번호]
    
    for i in range(len(genres)):
        if genres[i] in total.keys():
            total[genres[i]]+=plays[i]
            gen_dic[genres[i]].append((plays[i],i))
        else:
            total[genres[i]]=plays[i]
            gen_dic[genres[i]]=[(plays[i],i)]

        
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    for i in total:
        play = gen_dic[i[0]]
        play = sorted(play, key=lambda x: x[0], reverse=True)
        
        for i in range(2):
            answer.append(play[i][1])

    return answer

#런타임에러가 발생해였고 마지막 for문만 수정했는데
#통과가 된 코드
def solution(genres, plays):
    answer = []
    
    total={} #장르별 총 재생 횟수
    gen_dic={} #장르별 [재생 횟수 & 고유 번호]
    
    for i in range(len(genres)):
        if genres[i] in total.keys():
            total[genres[i]]+=plays[i]
            gen_dic[genres[i]].append((plays[i],i))
        else:
            total[genres[i]]=plays[i]
            gen_dic[genres[i]]=[(plays[i],i)]

    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    for i in total:
        play = gen_dic[i[0]]
        play = sorted(play, key=lambda x: x[0], reverse=True)
        
        for item in play[:2]:
            answer.append(item[1])

    return answer