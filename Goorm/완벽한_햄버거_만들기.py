# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
tasty = list(map(int, input().split()))

max_index = tasty.index(max(tasty))

for i in range(1, max_index):
	if tasty[i] < tasty[i-1]:
		print(0)
		exit()

for i in range(max_index+1, n):
	if tasty[i] > tasty[i-1]:
		print(0)
		exit()
		
print(sum(tasty))