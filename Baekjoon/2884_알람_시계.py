h, m = map(int, input().split())

time = h*60 + m
time -= 45

h = time // 60
if h < 0:
    h = 24+h
m = time % 60

print("%d %d" %(h, m))