def solution(n, m, section):
    paint, answer = section[0]-1, 0
    
    for i in section:
        if paint < i:
            paint = i+m-1
            answer += 1

    return answer