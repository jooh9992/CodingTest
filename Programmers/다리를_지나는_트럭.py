from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    a = 0 # 다리 위에 있는 트럭의 무게
    
    while bridge:
        a -= bridge.popleft() # 다리를 지나간 트럭은 무게에서 제외
        answer+=1 
        
        if truck_weights:
            if a + truck_weights[0] <= weight:
                a += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
        
    return answer