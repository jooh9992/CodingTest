N = int(input())
result = 0

if N // 14 >= 1:
	N -= (N//14)*14
	result += (N//14)

if N // 7 >= 1:
	a  = (N//7)
	N -= a*7
	result += a
	
result += N

print(result)