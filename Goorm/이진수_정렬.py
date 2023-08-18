# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, k = map(int,input().split())
a = list(map(int, input().split()))

count_arr = [(arr, format(arr, 'b').count('1')) for arr in a]

sort_count_arr = sorted(count_arr, key=lambda x: (x[1], x[0]), reverse = True)

print(sort_count_arr[k-1][0])