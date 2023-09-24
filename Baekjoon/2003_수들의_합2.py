import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
start = 0
end = 1

while end <= N:
    nums = arr[start:end]
    num = sum(nums)
    if num == M:
        answer += 1
        end += 1
    elif num < M:
        end+= 1
    else:
        start+= 1

print(answer)