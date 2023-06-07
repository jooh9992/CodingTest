import sys
input = sys.stdin.readline

arr = input().rstrip()
stack = []
val = 1
count = 0

for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(arr[i])
        val *= 2
    elif arr[i] == "[":
        stack.append(arr[i])
        val *= 3
    elif arr[i] == ")":
        if not stack or stack[-1] == "[":
            count = 0
            break
        if arr[i-1] == "(":
            count += val
        stack.pop()
        val //= 2
    else:
        if not stack or stack[-1] == "(":
            count =0
            break
        if arr[i-1] == "[":
            count += val
        stack.pop()
        val //= 3

if stack:
    print(0)
else:
    print(count)