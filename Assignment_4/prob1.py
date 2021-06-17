n = int(input())
a = map(int, input().split())
a = list(a)
a.sort()

for i in range(n-1,-1,-1):
    if a[i] > a[i-1]:
        print(a[i-1])
        break
