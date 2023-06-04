import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int,(input().rsplit()))
num = list(map(int, input().rsplit()))
D = deque()

for i in range(N):
    #슬라이딩 윈도우 범위를 벗어나는 원소 popleft
    if D and D[0][0] <= i-L:
        D.popleft()
    
    #들어올 원소가 기존의 원소보다 작으면 기존원소 pop
    while len(D) >=1 and num[i] < D[-1][1]:
        D.pop()

    D.append((i, num[i]))
    print(D[0][1], end=" ")
