def solution(numbers, target):
    nums = [0]
    
    for num in numbers:
        tmp = []
        for p in nums:
            tmp.append(p + num)
            tmp.append(p - num)
        nums = tmp
        
    return nums.count(target)