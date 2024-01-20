import heapq

def solution(operations):
    answer = []
    
    heap = []
    
    for i in operations:
        if i[0] == "I":
            heapq.heappush(heap, int(i[2:]))
        elif i == "D -1":
            if len(heap) != 0:
                heapq.heappop(heap)
        else:
            if len(heap) != 0:
                max_value = max(heap)
                heap.remove(max_value)
    
    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [max(heap), heapq.heappop(heap)]
        
    return answer