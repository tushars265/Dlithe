n = int(input())
rows = (n+1)//2
m= 1 + (rows - 2) * 2
j=1
for i in range(rows-1):
    print(" "*i, j," "* (m), n-j+1, sep='')
    j += 1
    m=m-2
print(" "*(rows-2), rows)
