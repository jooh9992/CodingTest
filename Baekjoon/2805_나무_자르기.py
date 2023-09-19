import sys
input = sys.stdin.readline

#나무 M미터가 필요. 절단기 높이 H 지정, 그 다음 한줄에 연속해있는 나무 모두 절단
# 20, 15, 10, 17 이고 H가 15이면 15, 15, 10, 15 으로 5, 2 총 7미터를 집에 들고 감

N , M = map(int, input().split())
arr = list(map(int, input().split()))
start = 1
end = max(arr)

while start <= end:
    mid = (start+end) // 2
    count = 0

    for i in arr:
        if i >= mid:
            count += i -mid
    
    if count >= M:
        start = mid + 1
    else:
        end = mid -1
print(end)