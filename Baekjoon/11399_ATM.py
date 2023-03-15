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