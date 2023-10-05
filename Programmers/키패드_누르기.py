def solution(numbers, hand):
    answer = ''
    num = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)}
    
    r = num['#']
    l = num['*']
    
    for i in numbers:
        if i in [1, 4, 7]:
            l = num[str(i)]
            answer += 'L'
        elif i in [3, 6, 9]:
            r = num[str(i)]
            answer += 'R'
        else:
            l_d = abs(l[0] - num[str(i)][0]) + abs(l[1] - num[str(i)][1])
            r_d = abs(r[0] - num[str(i)][0]) + abs(r[1] - num[str(i)][1])
            
            if l_d < r_d:
                l = num[str(i)]
                answer += 'L'
            elif l_d > r_d:
                r = num[str(i)]
                answer += 'R'
            else:
                if hand == 'right':
                    r = num[str(i)]
                    answer += 'R'
                else:
                    l = num[str(i)]
                    answer += 'L'
    
    return answer