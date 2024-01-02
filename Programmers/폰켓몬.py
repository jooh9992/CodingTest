def solution(nums):
    answer = 0
    a = set(nums)
    
    if len(a) >= (len(nums)//2):
        answer = len(nums)//2
    else:
        answer = len(a)
    
    return answer

#24/01/02
def solution(nums):
    answer = 0
    
    a = len(nums)//2
    b = len(set(nums))
    
    return min(a, b)