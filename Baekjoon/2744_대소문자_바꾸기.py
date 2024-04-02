li = input()
answer = ""

for i in li:
    if ord(i) > 90:
        answer += chr(ord(i)-32)
    else:
        answer += chr(ord(i)+32)

print(answer)