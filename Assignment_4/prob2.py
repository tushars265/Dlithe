string = input()
n = int(input())
d = []
r = []
for i in range(n):
    a, b = input().split()
    d.append(a)
    r.append(int(b))

strlen = len(string)
substring = ""
for i in range(n):
    if d[i] == 'L':
        substring += string[r[i]]
    else:
        substring += string[strlen - r[i]]

sublen = len(substring)
flag = 0
for i in range(strlen - sublen):
    count = 0
    for j in range(sublen):
        if substring[j] not in string[i:sublen]:
            break
        else:
            count += 1
    if count == sublen:
        print("Yes")
        flag = 1
        break
if flag == 0:
    print("No")

