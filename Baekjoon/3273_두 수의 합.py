a = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
start, end = 0, a-1
cnt, tmp = 0, 0

while start < end:
    tmp = arr[start] + arr[end]
    if tmp == x:
        cnt += 1
        start += 1
        end -= 1
    elif tmp > x:
        end -= 1
    else:
        start += 1
print(cnt)