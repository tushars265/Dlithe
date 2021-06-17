# Problem 1.
#   Write a prorgram to calculate simple interest.
# 	formula to calculate simple interest : PNR/100

principal = float(input ("Enter principal amount : "))
time = float (input("Enter Time : "))
Rate = float(input("Enter rate : "))

print("Simple Interest = ",principal*time*Rate/100)