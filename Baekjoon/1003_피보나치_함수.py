import sys
input = sys.stdin.readline

t = int(input())
zero = [1,0,1]
one = [0,1,1]

def fibo(n):
    if len(zero) <= n :
        for i in range(len(zero), n+1) :
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])

for i in range(t):
    a = int(input())
    fibo(a)