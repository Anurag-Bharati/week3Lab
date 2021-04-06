# For given int x, print True, False and Zero if x is Positive, Negative and zero.

w2_num_check = int(input("Enter a number: "))
if w2_num_check == 0:
    print("Zero")
else:
    print(w2_num_check > 0 and not w2_num_check < 0)        # Logic :P



