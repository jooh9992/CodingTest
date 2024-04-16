def solution(numbers):
    answer = []
    
    for i in numbers:
        if i % 2 == 0:
            answer.append(i+1)
        else:
            #가장 마지막 0을 찾아서 그것을 1로 바꾸고 그 다음 수를 0으로 바꿈
            num = '0' + bin(i)[2:]
            idx = num.rfind("0")
            nums = list(num)
            nums[idx] = "1"
            nums[idx+1] = "0"
            
            num2 = "".join(nums)
            
            answer.append(int(num2, 2))
    
    return answer