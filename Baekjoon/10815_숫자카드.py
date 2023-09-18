import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

def bs(x):
    low = 0
    high = N -1

    while low <= high:
        mid = (low + high) // 2

        if N_list[mid] == x:
            return 1
        elif x < N_list[mid]:
            high = mid -1
        else:
            low = mid + 1
    return 0

for i in M_list:
    print(bs(i), end=' ')