a = int(input())
arr = [0]*a
cnt = 0

def board(n):
  for i in range(n):
    if arr[n] == arr[i] or abs(arr[n] - arr[i]) == abs(n -i):
      return 0
  return 1

def func(n):
  global cnt

  if n == a:
    cnt += 1
    return

  else:
    for i in range(a):
        arr[n] = i
        if board(n):
            func(n + 1)

func(0)
print(cnt)