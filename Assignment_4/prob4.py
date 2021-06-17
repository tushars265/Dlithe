n = int(input())
a = list(map(int, input().split()))

flag = 0
flag1 = 0
flag2 = 0
flag3 = 0
for i in range(n-1):
    if a[i] < a[i+1]:
        flag1 = 1
        if flag2 == 1 or flag3 == 1:
            print("No")
            flag = 1
            break
    elif a[i] == a[i+1]:
        flag2 = 1
        if flag3 == 1:
            print("No")
            flag = 1
            break
    else:
        flag3 = 1
if flag == 0:
    print("Yes")