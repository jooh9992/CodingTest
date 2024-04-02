import sys
from collections import deque
input = sys.stdin.readline

#오른쪽 톱니바퀴 확인
def right(idx, way):
    if idx > 3:
        return
    if top[idx-1][2] != top[idx][6]:
        right(idx+1, -way)
        top[idx].rotate(way)

#왼쪽 톱니바퀴 확인
def left(idx, way):
    if idx < 0:
        return
    if top[idx][2] != top[idx+1][6]:
        left(idx-1, -way)
        top[idx].rotate(way)       

# 톱니바퀴 상태
top = [deque(list(map(int,input().rstrip()))) for _ in range(4)]

# 회전 횟수
k = int(input())

for _ in range(k):
    idx, way = map(int, input().split())
    idx -= 1

    left(idx-1, -way)
    right(idx+1, -way)

    top[idx].rotate(way)

# 점수계산
answer = 0
if top[0][0] == 1:
	answer+=1
if top[1][0] == 1:
	answer+=2
if top[2][0] == 1:
	answer+=4
if top[3][0] ==1:
	answer+=8
     
print(answer)