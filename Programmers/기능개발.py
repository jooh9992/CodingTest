import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    a = 0
    
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100-p)/s))
    
    while days:
        day = days.popleft()
        if day > a:
            answer.append(1)
            a = day
        else:
            answer[-1] += 1
    
    return answer