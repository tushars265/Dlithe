def checkprime(n):

    for i in range(2, n//2+1):
         if n % i == 0 :
             return False
    return True

num = int(input())
sum = 2

for i in range(3, num):
    if checkprime(i):
        sum = sum + i
        if sum > num:
            break
        if checkprime(sum):
            print(sum, end=" ")
