stu = [i for i in range(1, 31)]

for _ in range(28):
    a = int(input())
    stu.remove(a)

for i in stu:
    print(i)