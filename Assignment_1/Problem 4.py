# Problem 4:
# 	Read three integers from the keyboard a,b,c and those values in the following order.
#
#   max > mid > min
#
#   Sample Input
#   10 1 7
#
#   Sample Output
#   10 > 7 > 1

a,b,c=map(int ,input().split())
maxim = max(a,b,c)
mini = min(a,b,c)
mid = a+b+c-maxim-mini
print(maxim,mid,mini,sep=' > ')