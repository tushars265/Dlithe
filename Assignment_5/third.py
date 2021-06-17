n = int(input())
a = []
b = []
for i in range(n):
    ab = list(map(int, input().split()))
    a.append(ab)

b.append(a[0])

for i in range(1,n):
    flag = 0
    for j in range(len(b)):
         if (b[j][0] >= a[i][0] and b[j][0] <= (a[i][1]+ a[i][0])) or ((b[j][1]+b[j][0]) >= a[i][0] and (b[j][1]+b[j][0]) <= (a[i][1]+ a[i][0])):
             continue
         else:
             flag = 1
             break
    if flag == 0:
        b.append(a[i])
print(len(b))