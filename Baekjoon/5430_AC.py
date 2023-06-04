import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))

    flag = 0    
    if n == 0:
        arr = []
    
    for i in p:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if len(arr) == 0:
                print('error')
                break
            else:
                if flag % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
    
    else:
        if flag % 2 == 1:
            arr.reverse()
        print('[' + ','.join(arr) +']')       