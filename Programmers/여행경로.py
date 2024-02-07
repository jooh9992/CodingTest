from collections import deque

def solution(tickets):
    answer = []
    #BFS를 위한 큐 [(현재공항, 공항 경로, 사용한 티켓 번호)]
    queue = deque([("ICN", ["ICN"], [])])

    while queue:
        airport, path, used = queue.popleft()

        if len(used) == len(tickets): #사용한 티켓수와 가진 티켓 수가 같을 때 공항 경로를 answer에 저장
            answer.append(path)
        
        for idx, ticket in enumerate(tickets): 
            if ticket[0] == airport and not idx in used: #티켓의 출발지와 현재공항이 맞고 사용한 티켓이 아닐 때
                queue.append((ticket[1], path+[ticket[1]], used+[idx])) #티켓의 도착지를 추가
    
    answer.sort() #알파벳 순서를 출력하기 위해 정렬

    return answer[0]