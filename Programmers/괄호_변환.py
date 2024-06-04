#분리
def finds(p):
    l, r = 0, 0
    
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            return p[:i + 1], p[i + 1:]
        
#올바른 괄호 문자열 확인
def check(u):
    stack = []
    
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    
    return True
    

def solution(p):    
    if p == '':
        return ''
    
    u, v = finds(p)
    
    if check(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        
        for i in u[1: len(u)-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
        return answer