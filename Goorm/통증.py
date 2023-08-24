N = int(input())
result = 0

if N // 14 >= 1:
	a  = (N//14)
	N -= a*14
	result += a

if N // 7 >= 1:
	a  = (N//7)
	N -= a*7
	result += a
	
result += N

print(result)