# Check whether the given year is leap year or not. (Note year exactly divide by 4 is leap year)

main = True

while main:

    main = False
    w2_Year = int(input("Enter the year: "))

    if len(str(w2_Year)) == 4:

        if ((w2_Year % 4 == 0) and (w2_Year % 100 != 0)) or (w2_Year % 400 == 0):
            print("LEAP YEAR!")
        else:
            print("COMMON YEAR!")

    else:
        print("Please enter a valid year!")
        main = True
