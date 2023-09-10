from sys import stdin

n = int(stdin.readline())

p = list(map(int, stdin.readline().split()))
p.sort()

answer = 0
an = 0

for i in p:
    an += i
    answer += an

print(answer)

#23/09/10 다시 풀기

import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
sum = 0
result = 0

p.sort()

for i in p:
    sum += i
    result += sum

print(result)