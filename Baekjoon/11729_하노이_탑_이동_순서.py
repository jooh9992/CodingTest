import sys
input = sys.stdin.readline

def hanoi(n, a, b):
    if n>1:
        hanoi(n-1, a, 6-a-b)
    print(a, b)
    if n>1:
        hanoi(n-1, 6-a-b, b)

N = int(input())
print(2**N -1)
hanoi(N, 1, 3)