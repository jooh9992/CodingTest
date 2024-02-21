# Counter와 딕셔너리를 사용한 풀이
from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for i in range(len(discount) - 9):
        if dic == Counter(discount[i:i+10]):
              answer += 1
            
    return answer

# all을 사용하여 비교
def solution(want, number, discount):
    answer = 0
    N = len(discount)
    i = 0
    
    while i + 10 <= N:
        discount_ten = discount[i: i+10]
        
        # 모든 poroduct의 개수가 num과 같을 때 참을 반환
        if all(num == discount_ten.count(product) for product, num in zip(want, number)):
            answer += 1
        
        i += 1
    
    return answer