import random
times=int(input("Enter the no.of times:"))
for i in range(times):
    n=input("Do you want to role?(YES/NO):")
    if n=="YES":
        print("Roll",i+1)
        print(random.randint(1,6))
    else:
        break
