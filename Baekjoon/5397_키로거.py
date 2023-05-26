import sys
input = sys.stdin.readline

num = int(input())

for i in range(num):
  test = input().strip()
  stack1, stack2 = [], []

  for j in test:
    if j == '<':
      if stack1:
        stack2.append(stack1.pop())
    elif j == '>':
      if stack2:
        stack1.append(stack2.pop())
    elif j == '-':
      if stack1:
        stack1.pop()
    else:
      stack1.append(j)

  print("".join(stack1 + list(reversed(stack2))))