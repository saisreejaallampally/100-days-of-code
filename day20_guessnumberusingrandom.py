import random
print("Guess the number:")
comp_num=random.randint(1,10)
times=int(input("Enter the number max number of guesses:"))

for i in range(times):
    guess_num=int(input("Enter a number between 1 to 10:"))
    if guess_num==comp_num:
        print(f"guessed in {i+1} times")
        break
    elif guess_num>comp_num:
        print("Guess too high")
    elif guess_num<comp_num:
        print("Guess too low")
    else:
        print("Better luck next time")
        
        