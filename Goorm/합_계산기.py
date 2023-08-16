# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
t = int(input())
ans = 0

for i in range(t):
	n, a, m = input().split()
	if a == '+':
		ans += (int(n)+int(m))
	elif a == '-':
		ans += (int(n)-int(m))
	elif a == '*':
		ans += (int(n)*int(m))
	elif a == '/':
		ans += (int(n)//int(m))
print(ans)