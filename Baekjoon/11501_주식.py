import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max = 0
    result = 0

    for i in range(len(arr)-1, -1, -1):
        if (arr[i] > max):
            max = arr[i]
        else:
            result += max-arr[i]
    print(result)
    