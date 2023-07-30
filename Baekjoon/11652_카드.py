import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
    tmp = int(input())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

dic = sorted(dic.items(), key= lambda x:(-x[1], x[0]))
print(dic[0][0])

# 최빈값을 구하는 mode 함수를 사용하는 방법
from statistics import *

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
print(mode(arr))