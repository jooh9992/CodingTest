#투 포인터를 사용해서
#구명보트에 몸무게가 제일 큰 사람과 제일 작은 사람을 더해서 비교
def solution(people, limit):
    answer = 0
    people.sort()
    
    a = 0
    b = len(people) -1
    
    while a < b:
        if people[b] + people[a] <= limit:
            a -= 1
            answer += 1
        
        b -=1
    
    return len(people) - answer