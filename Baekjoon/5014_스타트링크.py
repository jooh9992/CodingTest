import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft() #시작위치
        if v == G:
            return count[G]
        for i in (v+U, v-D): #U만큼 위로 or D만큼 아래로
            if 0 < i <= F and not visited[i]:
                visited[i] = 1 #방문한 층은 1
                count[i] = count[v] + 1 #층까지의 이동 횟수를 저장
                q.append(i)
    if count[G] == 0:
        return "use the stairs"

F, S, G, U, D = map(int, input().split())
visited = [0 for i in range(F+1)]
count = [0 for i in range(F+1)]
print(bfs(S))