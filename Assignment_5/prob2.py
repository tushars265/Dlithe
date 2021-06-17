a = list(map(int, input().split()))
n = len(a)
count = 1
b = [1]
c = [1]
for i in range(1,n):
     if a[i] <=  a[i - 1]:
         count = 1
     else:
         count = count + 1
     b.append(count)
count = 1
d = a[::-1]
for i in range(1,n):

     if d[i] <=  d[i - 1]:
         count = 1
     else:
         count = count + 1
     c.append(count)
c = c[::-1]
sum = 0
for i in range(0,n):
    if c[i] >= b[i]:
        sum += c[i]
        print(c[i],end=" ")
    else:
        sum += b[i]
        print(b[i], end=" ")
print()
print(sum)