def solution(k, tangerine):
    answer = 0
    t_list = [0]*max(tangerine)
    
    for i in tangerine:
        t_list[i-1] += 1
        
    t_list.sort(reverse=True)
    
    for i in t_list:
        k -= i
        answer += 1
        if k <= 0:
            return answer
            

# 다른 사람의 풀이를 봤는데 Counter를 사용한 풀이가 있었다.
# python은 이런 점이 좋은데 공부해서 꼭 counter를 사용해야지!
import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer