# Give three int and print the smallest one.

w2_numList = [int(input("Enter a number: ")),
              int(input("Enter the second number: ")),
              int(input("Enter the third one: "))]
w2_numList.sort()
print(f"The smallest number is {w2_numList[0]}")
