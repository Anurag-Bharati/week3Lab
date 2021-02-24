# WAP to enter name and age

userName = str(input("Enter your name: "))
userAge = int(input("Enter your age: "))

print(f"My name is {userName} and my age is {userAge}.")
print("My name is", userName, "and my age is", userAge, ".")
print("My name is " + userName + " and my age is " + str(userAge) + ".")

userinfo = [userName, userAge]

print("My name is", userinfo[0], "and my age is", userinfo[1], ".")
print("My name is {} and my age is {}.".format(userName, userAge))
