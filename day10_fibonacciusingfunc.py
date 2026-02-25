def fibonacci(n):
    i=0
    j=1
    count=1
    while count<=n:
        print(i)
        next=i+j
        i=j
        j=next
        count=count+1
fibonacci(5)
        
