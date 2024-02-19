def solution(elements):
    answer = set()
    cnt = len(elements)
    
    for i in range(1, cnt+1):
        for j in range(cnt):
            if i+j > cnt:
                answer.add(sum(elements[i:]+ elements[:i+j-cnt]))
            else:
                answer.add(sum(elements[j:i+j]))

    return len(answer)