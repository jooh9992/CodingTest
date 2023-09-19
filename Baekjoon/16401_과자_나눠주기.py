import sys
input = sys.stdin.readline

M , N = map(int, input().split())
arr = list(map(int, input().split()))
start = 1
end = int(1e9)
answer = 0

while start <= end:
    mid = (start+end)//2
    count = 0
    for i in arr:
        count += i //mid
    if count >= M:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)