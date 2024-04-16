from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt1 = sum(queue1)
    cnt2 = sum(queue2)
    limit = len(queue1) + len(queue2)
    answer = 0

    if (cnt1 + cnt2) % 2 == 1:
        return -1
    
    while cnt1 != cnt2:
        if answer > limit:
            return -1
        
        while queue1 and cnt1 > cnt2:
            a = queue1.popleft()
            queue2.append(a)
            answer += 1
            cnt1 -= a
            cnt2 += a
            
        while queue2 and cnt2 > cnt1:
            a = queue2.popleft()
            queue1.append(a)
            answer += 1
            cnt2 -= a
            cnt1 += a
    
    return answer