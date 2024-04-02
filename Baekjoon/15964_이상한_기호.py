def mat(a, b):
    return ((a+b)*(a-b))

a, b = map(int, input().split())
print(mat(a,b))