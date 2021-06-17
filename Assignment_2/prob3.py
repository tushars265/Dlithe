# Write a program to calculate the EB Bill.
#
# The tariff rate for all division is the same. Karnataka electricity board single slaps for the domestic LT supply such as for 0 to 30 units the per-unit cost will be ? 3.75/-, from 31 to 100 the per-unit cost will be ? 5.20, from 101 to 200, the per-unit cost will be ? 6.75 and above 201 units you have to pay ? 7.8 per unit.
# Additionally, the consumer will pay fixed charges as ? 60/- and electricity tax of 5% extra.
units = int(input())

if units <= 30:
    cost = 3.75
elif units <=100:
    cost = 5.2
elif units <= 200:
    cost = 6.75
else:
    cost = 7.8
amount = cost * units
tax = amount * 0.05
amount1 = amount + tax + 60
print("No of units          : %10.2f"%units)
print("Cost per unit        : %10.2f"%cost)
print("Amount               : %10.2f"%amount)
print("Fixed charges        : %10.2f"%60)
print("Electricity tax (5)  : %10.2f"%tax)
print("                       ----------")
print("Total Amount         : %10.2f"%amount1)
print("                       ----------")