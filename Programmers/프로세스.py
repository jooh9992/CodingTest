from collections import deque

def solution(priorities, location):
    answer = 0
    
    data = deque(enumerate(priorities))
    
    while data:
        i, priority = data.popleft()
        
        if any(priority < p for _, p in data):
            data.append((i, priority))
        
        else:
            answer += 1
            if i == location:
                break
    return answer