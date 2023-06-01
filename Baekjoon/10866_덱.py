import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = deque()

for i in range(N):
    command= input().split()
    
    if command[0] == "push_front":
        arr.appendleft(command[1])
    elif command[0] == "push_back":
        arr.append(command[1])
    elif command[0] == "pop_front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif command[0] == "pop_back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif command[0] == "size":
        print(len(arr))
    elif command[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0) 
    elif command[0] == "front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif command[0] == "back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1]) 