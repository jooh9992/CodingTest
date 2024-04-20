def solution(numbers, target):
    answer = 0
    num = [0]
    
    for i in numbers:
        temp = []
        
        for n in num:
            temp.append(n-i)
            temp.append(n+i)
        num = temp
    
    for n in num:
        if n == target:
            answer += 1
    
    return answer