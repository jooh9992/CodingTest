import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())

arr.sort(key = lambda x : int(x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])