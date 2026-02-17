import random
print("Welcome to Guess the number game!")
print("I have chosen a number between 0 and 100\nTry to guess it!")
secret=random.randint(1,100)
guess=int(input("enter your guess:"))
attempts=1
while guess!=secret:
    if guess>secret:
        print("Too high")
        
    else:
        print("Too low")
    attempts=attempts+1
    guess=int(input("try again:"))
print("correct guess")
print(f"Guessed in {attempts} attempts")
    