t = int(input())

for _ in range(t):
    answer = 0
    i = 1
    q = input()

    for j in q:
        if j == "O":
            answer += i
            i += 1
        else:
            i = 1
    
    print(answer)