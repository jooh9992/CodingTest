from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    
    for i in range(len(s)):
        s.rotate(-1)
        check = []
        
        for j in s:
            if len(check) == 0:
                check.append(j)
            else:
                check.append(j)
                if check[-2] == "(" and check[-1] == ")":
                    check.pop()
                    check.pop()
                elif check[-2] == "[" and check[-1] == "]":
                    check.pop()
                    check.pop()
                elif check[-2] == "{" and check[-1] == "}":
                    check.pop()
                    check.pop()

        if len(check) == 0:
            answer += 1

    return answer