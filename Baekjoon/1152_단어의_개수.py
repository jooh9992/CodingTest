t = input()
answer = 0

for i in t.split(" "):
    if i.isalpha():
        answer += 1

print(answer)