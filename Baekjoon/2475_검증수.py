def squa(a):
    return a**2

li = list(map(int, input().split()))
answer = 0

for i in li:
    answer += squa(i)

print(answer%10)