from sys import stdin

n = int(stdin.readline())
times = []
for i in range(n):
    s, e = map(int, stdin.readline().split())
    times.append([s, e])

count = 0
times.sort(key = lambda x: (x[1], x[0]))
t =0
for i in range(n):
    if t > times[i][0]:
        continue
    count +=1
    t = int(times[i][1])

print(count)