# WAP to print the last digit

w2_input = str(int(input()))             # Converts entered data into string so that the values can be indexed later on.

w2_input_length = len(w2_input)             # Stores the entered data length

last_digit = w2_input[w2_input_length-1]    # Finds the index of last value

print(last_digit)                          # Prints it out.
