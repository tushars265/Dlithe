# Problem 2:
# 	Read three integers from the keyboard a,b,c, d and those values in the following order.
#
# max > mid1 > mid2 > min
#
# Sample Input
# 10 1 7 5
#
# Sample Output
# 10 > 7 > 5 > 1
a,b,c,d = map(int, input().split())

maxim = max(a,b,c)
mini = min(a,b,c)
mid = a+b+c-maxim-mini

if d > maxim:
    print(d,maxim,mid,mini,sep=' > ')
elif maxim > d and d > mid:
    print(maxim, d, mid, mini, sep=' > ')
elif mid > d and d > mini:
    print(maxim, mid, d, mini, sep=' > ')
else:
    print(maxim, mid, mini, d, sep=' > ')