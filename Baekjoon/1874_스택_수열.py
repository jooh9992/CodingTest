import sys
input = sys.stdin.readline

n = int(input())
answer = []
arr = []
cnt = 1
a = 0

for i in range(n):
    num = int(input())

    while cnt <= num:
        arr.append(cnt)
        answer.append("+")
        cnt += 1
    
    if arr[-1] == num:
        arr.pop()
        answer.append("-")
    else:
        a = -1

if a == 0:
    for i in answer:
        print(i)
else:
    print("NO")
