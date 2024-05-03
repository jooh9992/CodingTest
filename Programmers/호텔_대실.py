from heapq import heappop, heappush

def solution(book_time):
    answer = 1
    books = []
    
    for start, end in book_time:
        books.append((int(start[:2]) * 60 + int(start[3:]), int(end[:2]) * 60 + int(end[3:])))
    
    books.sort()
    heap = []
    for s, e in books:
        if not heap:
            heappush(heap,e+10)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)
    
    return answer
