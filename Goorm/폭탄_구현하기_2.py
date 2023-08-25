# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int, input().split())
m = [list(input().split()) for _ in range(N)]
z = []

dy = [0, 1, -1, 0, 0]
dx = [0, 0, 0, 1, -1]

score = [[0] * N for _ in range(N)]

for _ in range(K):
	y, x = map(int, input().split())
	y -= 1
	x -= 1
	
	for k in range(5):
		ny = y + dy[k]
		nx = x + dx[k]
		
		if ny < 0 or ny >= N or nx < 0 or nx >= N or m[ny][nx] == "#":
			continue
		
		if m[ny][nx] == "@":
			score[ny][nx] += 2
		else:
			score[ny][nx] += 1

result = 0

for i in range(N):
	for j in range(N):
		result = max(result, score[i][j])

print(result)