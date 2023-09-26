import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]

answer = 0

for i in range(N):
    if i+k > N :
        count = len(set(arr[i:N] + arr[:(i+k)%N] + [c]))
    else:
        count = len(set(arr[i: i+k] + [c]))
    if answer < count:
        answer = count

print(answer)