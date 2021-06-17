#idli and a girl
t=int(input())
for index in range(t) :
    a,b,k=map(int,input().split())
    n1=min(a,b)
    m=k//n1
    print(m)