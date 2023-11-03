#첫번째 방법 - 시간초과
def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].count(phone_book[i])>=1:
                answer = False
    
    return answer

#두번째 방법 - 접두어인 경우이기 때문에 sort를 사용해서 다음 단어와 비교
def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
            break
            
    return answer