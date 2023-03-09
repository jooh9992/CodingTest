def solution(a, b):
    answer = ''
    days = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    answer = weeks[(sum(days[:a-1])+b-1)%7] 
    return answer