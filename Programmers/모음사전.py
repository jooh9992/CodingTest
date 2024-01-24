from itertools import product
#product는 두개 이상의 리스트(or 집합) 끼리의 데카르트 곱(cartesian product)를 계산하여 iterator로 반환
# 1부터 5까지의 모든 조합에서 word 위치를 찾았다.
def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()
    
    return words.index(word) + 1