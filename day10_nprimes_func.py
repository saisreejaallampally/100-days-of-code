def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False
def primes_upto(m):
    for i in range(2,m+1):
        if is_prime(i):
            print(i)
primes_upto(20)