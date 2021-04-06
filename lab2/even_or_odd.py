# Check whether the user input number is even or odd and display it to user.

main = True

while main:

    main = False

    w2_check_num = int(input("Enter a number: "))

    if w2_check_num % 2 == 0 and w2_check_num != 0:
        print(f"\n{w2_check_num} is an even number.")

    elif w2_check_num % 2 != 0 and w2_check_num != 0:
        print(f"\n{w2_check_num} is a odd number.")

    elif w2_check_num == 0:
        print(f"0 does not considered as either even or odd.")
        main = True
