import sys, math
input = sys.stdin.readline

N = int(input())

# 에라토스테네스의 채
arr = [True]*(N+1)
arr[0] = False
arr[1] = False

for num in range(2, int(math.sqrt(N))+1):
    if arr[num]:
        for mul in range(num*2, N+1, num):
            arr[mul] = False

arr = [i for i in range(2, N+1) if arr[i]] + [0]

start = 0
end = 0
subtotal = arr[start]
count = 0

while end < len(arr)-1:
    if subtotal == N:
        count += 1
        subtotal -= arr[start]
        start += 1
        end += 1
        subtotal += arr[end]
    elif subtotal < N:
        end += 1
        subtotal += arr[end]
    else:
        subtotal -= arr[start]
        start += 1
        
print(count)