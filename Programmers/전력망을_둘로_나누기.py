#전선을 끊어서 두 전력망의 송전탑 개수를 비교하는 문제로
#DFS, BFS을 사용해서 완전 탐색을 하면 될 것같음
#아래의 코드는 DFS를 사용해서 해결

def DFS(start, graph, visited, check):
    cnt = 1
    visited[start]=True   #방문등록

    for adj_v in graph[start]:   #방문 이력 없고, 간선이 임시로 없앤 간선이 아닌 경우                                 
        if visited[adj_v] == False and check[start][adj_v]:    
            cnt += DFS(adj_v, graph, visited, check)
    return cnt                                                  

def solution(n, wires):
    answer = float("inf") 
    
    check = [[True]*(n+1) for _ in range(n+1)] # 끊은 전선인지 아닌지 체크하기 위한
    graph = [[] for _ in range(n+1)]   #송전탑 그래프
 
    for a,b in wires: # 송전탑 그래프 채우기
        graph[a].append(b)
        graph[b].append(a)
    
    for a,b in wires: # 송전탑의 전선을 다 확인하면서                               
        visited = [False]*(n+1) #두 전력망에 붙어 잇는 송접탑 개수를 세기 위해
        check[a][b] = False  #a에서 b로 가는 전선을 끊음                   
        cnt_a = DFS(a, graph, visited, check)  #a에 붙어 있는 송전탑 개수
        cnt_b = DFS(b, graph, visited, check)  #b에 붙어 있는 송전탑 개수
        check[a][b] = True  #a에서 b로 가는 전선을 다시 붙임                 
        
        answer = min(answer, abs(cnt_a - cnt_b))
    
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])