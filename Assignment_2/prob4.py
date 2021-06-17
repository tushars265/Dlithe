# rite a program to calculate the grade. The grade should be calculated in the following method.
#
# Constraints
# Score should be in between 1 to 100
#
# Score
# 	>= 90	 --> Grade O
# 	>= 80	--> Grade A+
# 	>= 70	--> Grade A
# 	>= 60	--> Grade B+
# 	>= 50	--> Grade B
# 	< 50	No Grade
# score = int(input())
# if score not in range(1,101):
#     print("Invalid")
# else:
#     if score >= 90:
#        print("Grade 0")
#     elif score >= 80:
#        print("Grade A+")
#     elif score >= 70:
#        print("Grade A")
#     elif score >= 60:
#        print("Grade B+")
#     elif score >= 50:
#        print("Grade B")
#     else:
#        print("No Grade")
strh = "Sdvsvs"
n=len(strh)
for i in range(n):
    print(strh[:n-i]," "*(2*i),strh[n-i-1::-1],sep="")




