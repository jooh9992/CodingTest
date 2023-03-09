def solution(t, p):
    answer = 0
    lenp = len(p)
    for i in range(len(t)-lenp+1):
        if int(t[i : i+lenp]) <= int(p):
            answer += 1
    return answer