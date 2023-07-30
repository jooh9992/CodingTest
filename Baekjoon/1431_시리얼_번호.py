import sys
input = sys.stdin.readline

def num(a):
    res = 0
    for i in a:
        if i.isdigit():
            res += int(i)
    return res

n = int(input())
arr = []

for i in range(n):
    arr.append(input().strip())

arr.sort(key=lambda x: (len(x),num(x), x))

for i in arr:
    print(i)