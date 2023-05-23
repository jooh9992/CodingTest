a = input()
cnt = [0]*10

for i in str(a):
    if (i == '6' or i =='9'):
        cnt[6] += 1
    else:
        cnt[int(i)] += 1
cnt[6] = (cnt[6]+1)//2

print(max(cnt))