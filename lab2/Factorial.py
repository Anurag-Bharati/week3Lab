# Given a positive real number, print its factorial.

w2_num = abs(int(input("Enter a number: ")))
factorial = 1
for i in range(1, w2_num+1):
    factorial *= i
print(factorial)
