import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = 0
start, end = 0, 0
check = [False]*100001

while start != N and end != N:
    if not check[arr[end]]:
        check[arr[end]] = True
        end += 1
        answer += end - start
    else:
        while check[arr[end]]:
            check[arr[start]] = False
            start += 1

print(answer)