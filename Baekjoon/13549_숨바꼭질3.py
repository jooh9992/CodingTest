import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
q.append(N) 
visited = [-1 for _ in range(100001)] #방문한 노드를 표시하기 위해 리스트 생성, 방문하지 않은 노드는 -1
visited[N] = 0 #시작점을 0으로 방문 표시

while q:
    s = q.popleft() 
    if s == K: #수빈이와 동생 위치가 같을 때 종료
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1] == -1: #s-1이 범위 안에 있고 방문 하지 않았을 때
        visited[s-1] = visited[s] + 1 #s까지의 이동 횟수에 1을 더해 s-1의 이동횟수로 저장
        q.append(s-1) #s-1을 q에 저장하면서 다음 탐색에서 s-1 노드를 방문해야 함을 의미
    if 0 < s*2 < 100001 and visited[s*2] == -1: #s*2가 범위 안에 있고 방문 하지 않았을 때
        visited[s*2] = visited[s] #0초만에 순간이동하기 때문에 s까지의 이동횟수를 2*s에 저장
        q.appendleft(s*2)  # 왼쪽에 저장함으로 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= s+1 < 100001 and visited[s+1] == -1:
        visited[s+1] = visited[s] + 1
        q.append(s+1)