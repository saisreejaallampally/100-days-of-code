def fibonacci(n):
    i=0
    j=1
    count=1
    arr=[]
    while count<=n:
        arr.append(i)
        next=i+j
        i=j
        j=next
        count=count+1
    return arr
print(fibonacci(10))
        
