um = list(map(int, input().split()))

if um == sorted(um):
    print("ascending")
elif um == sorted(um, reverse = True):
    print("descending")
else:
    print("mixed")