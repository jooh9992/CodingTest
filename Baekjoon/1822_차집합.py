import sys
input = sys.stdin.readline

A, B = map(int, input().split())
A_list = set(map(int, input().split()))
B_list = set(map(int, input().split()))

result = []

for i in A_list:
    if i not in B_list:
        result.append(i)

result.sort()

print(len(result))
if len(result) != 0:
    print(*(result))