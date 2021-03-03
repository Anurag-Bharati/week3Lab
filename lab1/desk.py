# A school decides to replace the desk in three classrooms. Each desk sits two students. Given the no of student in each
# class, print the smallest possible no of desk that can be purchased. The program should read three ints the no of stud
# in each three classes, a, b,c respectively


lr12 = int(input("Enter the no of student in lr12: "))
lr11 = int(input("Enter the no of student in lr11: "))
lr10 = int(input("Enter the no of student in lr10: "))

classA = (lr10/2) + lr10 % 2
classB = (lr11/2) + lr11 % 2
classC = (lr12/2) + lr12 % 2

print(f"The desk req in lr10, lr11 and lr12 is {int(classA)}, {int(classB)}, {int(classC)}.")


