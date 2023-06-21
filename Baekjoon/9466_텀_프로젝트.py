import sys
sys.setrecursionlimit(1000001)

input = sys.stdin.readline

def dfs(x,result):
    visited[x] = True
    team.append(x) #사이클을 이루는 팀을 확인하기 위해 현재 학생을 추가
    number = graph[x] # 현재 학생이 이동할 다음 학생의 인덱스를 가져옴
    
    if visited[number]: #이미 방문한 적이 있는지 확인
        if number in team: #사이클 가능 여부
            result += team[team.index(number):] #사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number,result)

for _ in range(int(input())):
    n =  int(input()) #학생 수
    graph = [0] + list(map(int,input().split())) #그래프 생성, 인덱스 맨 앞에 [0] 추가하여 접근편리하도록
    visited=[False for _ in range(n+1)] #방문 여부 저장
    result = [] #팀에 속하지 않은 학생들의 정보를 저장할 리스트 생성
    
    for i in range(1,n+1):
        if not visited[i]: #방문 안한 곳이라면
            team = [] #탐색 경로 정보를 저장할 stack 생성
            dfs(i,result) #DFS 함수 돌림
    
    print(n - len(result)) #팀에 없는 사람 수