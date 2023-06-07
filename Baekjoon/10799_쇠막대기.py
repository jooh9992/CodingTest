import sys
input = sys.stdin.readline

arr = input().rstrip()
stack = []
count = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
    else:
        if arr[i-1] =='(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)