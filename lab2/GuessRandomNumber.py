import random
n = random.randint(1, 10)
checkRight = True
attempts = 3
while checkRight:
    checkRight = False
    a = int(input("Guess a secret number: "))
    if a == n:
        print("You have guessed it correctly!! Congrats.")
        checkRight = False
        break
    elif a != n:
        attempts -= 1
        print(f"You have guessed it wrong. Now you have {attempts} Tries.")
        checkRight = True
        if attempts == 0:
            print("You have lost!!")
            print(f"The secret number was {n}")
            break
