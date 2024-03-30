word = input()
word = word.upper()

dic = {}

for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_count = max(dic.values())
max_chars = [char for char, count in dic.items() if count == max_count]

if len(max_chars) > 1:
    print("?")
else:
    print(max_chars[0])