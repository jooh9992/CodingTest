from heapq import heappop, heappush

def solution(N, road, K):
    answer = 0
    dist = [1e9] * (N+1)
    graph = [[] for _ in range(N+1)]
    
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))

    dist[1] = 0
    h = [(0,1)]
    
    while h:
        p, node = heappop(h)
        
        if dist[node] < p:
            continue
        
        for next_node, next_dis in graph[node]:
            d = p + next_dis
            if dist[next_node] > d:
                dist[next_node] = d
                heappush(h, (d,next_node))
    
    for d in dist[1:]:
        if d <= K:
            answer += 1
    
    return answer