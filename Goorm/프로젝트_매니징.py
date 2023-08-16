# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
t, m = map(int, input().split())
c = [int(input()) for i in range(n)]

T, m = divmod(m + sum(c), 60)
t = (t + T) % 24
print(t, m)