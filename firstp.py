import random
c=random.randint(1,100)
print("Guess a number between 1 and 100")   
while True:
    n=int(input("Enter your guess: "))
    if n<c:
        print("Too low! Try again.")
    elif n>c:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        break