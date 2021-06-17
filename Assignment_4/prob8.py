#check if a substring is present
subs  = (input())
string = (input())
l = string.split(subs)
m = "".join(l)
if m == string :
    print("no")
else :
    print("yes")