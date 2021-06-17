#print only the even number is gven in string
string=list(input().split())
for char in string :
    if len(char)%2==0:
        print(char)
