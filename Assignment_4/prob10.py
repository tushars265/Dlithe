#special char is present then don't accept that string
sen=input()
l=['@','_','!','#','$','%','^','&','*','(',')','<','>','?','/','|','{','}','~',':',]
for char in sen :
    if char in l:
        print ("string is not accepted")
        break
else :
    print("string is accepted")
