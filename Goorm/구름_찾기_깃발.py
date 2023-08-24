# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

N, K = map(int, input().split())

m = []

for _ in range(N):
	row = list(input().split())
	m.append(row)

result = 0

for i in range(N):
	for j in range(N):
		if m[i][j] == "1":
			continue
		
		check = 0
		
		for k in range(8):
			y = i + dy[k]
			x = j + dx[k]

			if y < 0 or y >= N or x < 0 or x >= N:
				continue
			
			if m[y][x] == "1":
				check += 1

		if check == K:
			result += 1

print(result)