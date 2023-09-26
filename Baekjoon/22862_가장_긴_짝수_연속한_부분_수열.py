import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
count = 0
tmp = 0
end = 0

for start in range(N):
    while (count <= K and end < N):
        if arr[end] %2 == 1:
            count +=1
        else:
            tmp +=1
        end += 1

        if start == 0 and end == N: #리스트가 홀수로만 이루어진 부분 수열 찾기
            answer = tmp
            break

    if count == K+1:
        answer = max(tmp, answer)
    
    if arr[start]%2 == 1:
        count -= 1
    else:
        tmp -=1
print(answer)