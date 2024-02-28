import sys
input = sys.stdin.readline

N = int(input())
i, num = 1, 1

while N > num:
    num += i *6
    i += 1

print(i)