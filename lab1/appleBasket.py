# WAP N students take K apple and distribute them amoung each other evenly. The remaning parts remains in the basket.
# how many apples will each single studnet get? and how many remains in the basket
# the program read the no.s N and K. It shouldprint the two ans
import math

appleInTheBasket = int(input("Enter the total no. of apples you bought: "))
numOfPeople = int(input("Enter the total no of student: "))
"""
appleDivided = appleInTheBasket//numOfPeople
appleRem = appleDivided % numOfPeople


print("Each student got: ", appleDivided)
print("Remaining apples: ", appleRem)

"""
checkIfTrue = True
while checkIfTrue:
    checkIfTrue = False
    if appleInTheBasket == numOfPeople:
        print("Every student gets one apple")
    elif appleInTheBasket > numOfPeople:
        print("Every student gets ", appleInTheBasket//numOfPeople)
    elif appleInTheBasket < numOfPeople:
        print()
