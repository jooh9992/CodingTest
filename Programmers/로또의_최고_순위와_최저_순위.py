def solution(lottos, win_nums):
    count = 0
    zeros = lottos.count(0)
    rank=[6,6,5,4,3,2,1]
    
    for i in lottos:
        if i in win_nums:
            count +=1
        
    return rank[count+zeros], rank[count]