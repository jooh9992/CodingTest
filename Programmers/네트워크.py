# DFS방법
# 같은 네트워크 상에 있는 컴퓨터를 찾기 위해서
# DFS 방법으로 하나씩 다 연결되어있는지 재귀하여 찾고
# 같은 네트워크 상에서 나올 때! answer +1 해줌
def solution(n, computers):
    
    def DFS(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)
    
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
    
    return answer