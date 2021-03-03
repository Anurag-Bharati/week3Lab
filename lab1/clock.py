# Given the int N - the no. of min that passed since midnight - how many hours and min are displayed on the 24 hr clock.
# The program should print two no: the no of hours (betn 0 and 23) and the no. of min (between 0 and 59)
N = int(input("Enter the minutes passed since midnight: "))
hours = (N//60)     # divide
minutes = (N%60)    # reminder
print(f"The hour is {hours} ")
print(f"The min is {minutes} ")
print(f"Its {hours}:{minutes} now.")
