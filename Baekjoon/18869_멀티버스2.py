import sys
input = sys.stdin.readline
from collections import defaultdict

M, N = map(int, input().split())
answer = defaultdict(int) #기본값을 int 0으로 지정

for _ in range(M):
    arr = list(map(int, input().split()))
    arr2 = sorted(list(set(arr)))
    dic = {arr2[i]:i for i in range(len(arr2))}
    vector = tuple([dic[i] for i in arr])
    answer[vector] += 1

sum = 0

for i in answer.values():
    sum += (i * (i-1)) //2

print(sum)