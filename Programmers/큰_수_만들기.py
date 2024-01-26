# 스택을 이용해서 해결
def solution(number, k):
    answer = []
    
    for num in number:
        while answer and answer[-1] < num and k > 0:
            k -= 1
            answer.pop()
        answer.append(num)

    #만약 "33111" , k =1 테케일 때의 예외처리
    #k수만큼의 뒤를 없애주도록함        
    if k != 0:
        answer = answer[:-k]
    
    return ''.join(answer)