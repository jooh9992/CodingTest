import sys

stack1 = list(sys.stdin.readline().rstrip())
stack2 = []
num = int(sys.stdin.readline().strip())

cursor = len(stack1)

for i in range(num):
  c = sys.stdin.readline().split()
  if c[0] == "P":
    stack1.append(c[1])
  elif c[0] == "L" and stack1:
    stack2.append(stack1.pop())
  elif c[0] == "D" and stack2:
    stack1.append(stack2.pop())
  elif c[0] == "B" and stack1:
    stack1.pop()

print("".join(stack1 + list(reversed(stack2))))