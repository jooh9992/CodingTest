def solution(n):
    answer = 0
    left, right, cnt = 0,0,0

    while left < n:
        if cnt < n:
            right += 1
            cnt += right
        else:
            if cnt == n: answer +=1
            left += 1
            cnt -= left

    return answer