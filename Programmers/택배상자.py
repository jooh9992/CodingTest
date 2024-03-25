from collections import deque  

def solution(order):  
    order = deque(order)  
    stack = []  
    answer = 0
    
    for i in range(1, len(order) + 1):  
        stack.append(i)
        while stack:  
            if order and stack[-1] == order[0]:
                stack.pop()  
                order.popleft()  
                answer += 1
            else:
                break

    return answer