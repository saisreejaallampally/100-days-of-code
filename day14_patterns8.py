n=int(input("Enter the no. of rows:"))
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("* " ,end="")
    print()
for i in range(1,n+1):
    for s in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("* ",end="")
    print()