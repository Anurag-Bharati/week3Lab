# Given a positive real number, print its factorial.

# w2_num = abs(int(input("Enter a number: ")))
factorial = 1


def fact(w2_num):

    global factorial
    for i in range(2, w2_num+1):
        factorial *= i
    return factorial


fact(5)

print(factorial)
