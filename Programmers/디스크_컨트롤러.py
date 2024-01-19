import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0 #소요시간 합, 현재 시간, 다음시간
    start = -1 
    heap = []
    
    while i < len(jobs):
        #매 작업이 끝나는 시점마다 끝나기 전에 요청된 작업 리스트를 갱신
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
                
        # 처리할 작업이 있는 경우
        if len(heap) > 0: 
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 종료시간에서 요청시간을 제외해서 작업 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)