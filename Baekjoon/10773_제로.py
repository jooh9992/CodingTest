import sys
input = sys.stdin.readline

k = int(input())
stack = []

for i in range(k):
    command = int(input())

    if command == 0:
        stack.pop()
    else:
        stack.append(command)
print(sum(stack))
