from sys import stdin

arr = stdin.readline().split('-')
answer = 0

for i in arr[0].split('+'):
    answer += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)

#23/09/11 다시풀기
import sys
input = sys.stdin.readline

arr = input().split('-')
sum = 0

for i in arr[0].split('+'):
    sum += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)