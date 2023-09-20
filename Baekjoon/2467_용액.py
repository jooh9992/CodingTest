import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

start = 0
end = len(arr)-1
value = 2000000000
a, b = 0, 0

while start < end:
    v = arr[start] + arr[end]

    if abs(v) <= value:
        a = arr[start]
        b = arr[end]
        value = abs(v)
    
    if v <= 0:
        start += 1
    else:
        end -= 1

print(a, b)