test = int(input())
while test>0:
    a, b, k = map(int, input().split())
    if a > b:
        a = b
    print(k // a)
    test -= 1
