# Given 3 digit number. Find out sum of its number

"""w2_number = str(int(input("Enter 3-digit number: ")))

w2_sum_3 = int(w2_number[0]) + int(w2_number[1]) + int(w2_number[2])

print(w2_sum_3)"""


def lstsum(lst):
    value = 0
    for i in range(len(lst)):
        value += lst[i]
    return value


lst = [1, 2, 4, 5, 6]
print(lstsum(lst))
