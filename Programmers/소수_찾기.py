from itertools import permutations

#소수 판별을 위한 함수 생성
#에라토스테네스의 체 사용
#약수를 판단할 때 2부터 n-1까지 반복할 필요가 없고
#해당 수의 제곱근을 기준으로 대칭을 이루기 때문에 제급근까지 계산하면 시간 복잡도에 도움이 됨
def check(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True

def solution(numbers):
    answer = 0
    nums = [i for i in numbers] #숫자를 리스트
    new_nums = set() #중복된 값을 제거하기 위해서 set으로 생성
    
    for i in range(1, len(numbers)+1):
        permutationList = permutations(nums, i) #1부터 len(numbers)+1까지의 개수로 순열사용
        for p in permutationList: #순열된 값으로 숫자를 만들어서 set에 넣어줌
            num = int(''.join(p))
            new_nums.add(num)
        
    for n in new_nums: #소수 판별하여 정답 도출
        if check(n):
            answer+=1
    
    return answer