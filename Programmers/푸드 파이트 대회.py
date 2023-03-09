def solution(food):
    answer = ''
    t = ''

    for i in range(1, len(food)):
        t += str(i) * (food[i] // 2)
    answer = ''.join(reversed(list(t)))
    return t+"0"+answer