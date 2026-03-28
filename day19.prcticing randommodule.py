import random
times=int(input("Enter the no. of times:"))
for i in range(times):
    a=input("Do you want to continue?:")   
    if a=="yes":
        m=int(input("Enter the value of m:"))
        n=int(input("Enter the value of n:"))
        print(random.randint(m,n))
    else:
        break
    