from itertools import permutations
from collections import deque
    
def calculate(exp,op):
    array= deque()
    tmp=""
    
    for i in exp:
        if i.isdigit():
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    array.append(tmp)
    
    for o in op:
        stack=[]
        while len(array)!=0:
            tmp=array.popleft()
            if tmp==o:
                result = str(eval(stack.pop()+o+array.popleft()))
                stack.append(result)
            else:
                stack.append(tmp)
        array = deque(stack)
            
    return abs(int(array.pop()))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result=[]
    
    for i in op:
        result.append(calculate(expression, i))
        
    return max(result)