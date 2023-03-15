from sys import stdin

n = int(stdin.readline())
weight = []
for i in range(n):
    value = int(stdin.readline())
    weight.append(value)

weight.sort(reverse=True)
answer = weight[i]*(i+1)

for i in range(0, n-1):
    if answer < weight[i+1]*(i+2):
       answer = weight[i+1]*(i+2)

print(answer)