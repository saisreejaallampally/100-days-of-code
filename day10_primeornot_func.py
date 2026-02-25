def prime_or_not(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return "prime"
    else:
        return "not prime"
print(prime_or_not(5))
        