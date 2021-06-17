n = int(input())
num = 0
for i in range(n-1):
    #print((i+1)*int("1"*(i+1)))
    num = num + 10 ** i
    print(num*(i+1))