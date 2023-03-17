from sys import stdin

n = int(stdin.readline())
mon = []

#날짜 계산을 하기 쉽게 100을 곱해서 날짜형식을 만들어서 입력
for i in range(n):
    start_m, start_d, end_m, end_d = map(int, stdin.readline().split())
    mon.append([start_m * 100 + start_d, end_m * 100 + end_d])

#오름차순으로 정렬
mon.sort()

#끝나는 날짜를 301로 초기화
target = 301
end =0
count = 0
#꽃 전체를 순회
while mon:
    #끝나는 날짜가 12월1일을 넘거나 시작날짜 301을 넘으면 break
    if target >= 1201 or mon[0][0] > target:
        break

    for i in range(len(mon)):
        if target >= mon[0][0]:
            if end <= mon[0][1]:
                end = mon[0][1]

            mon.remove(mon[0])
        else:
            break

    target = end
    count += 1

if target <1201:
    print(0)
else:
    print(count)