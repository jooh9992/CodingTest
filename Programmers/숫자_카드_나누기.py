from math import gcd
from functools import reduce

def na(arr, num):
    for i in arr:
        if i % num == 0:
            return True
    return False
    
def solution(arrayA, arrayB):
    answer = []
    
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))

    gcd_a = reduce(gcd, arrayA)
    gcd_b = reduce(gcd, arrayB)
    
    a = na(arrayB, gcd_a)
    b = na(arrayA, gcd_b)

    if not a:
        answer.append(gcd_a)
    if not b:
        answer.append(gcd_b)
    
    if answer:
        return max(answer)
    else:
        return 0