t = int(input())

for _ in range(t):
    r, s = input().split()
    answer = ""
    
    for i in s:
        answer += i*r
    
    print(answer)