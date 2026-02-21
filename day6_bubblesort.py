n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    
    ele=int(input(f"Enter element {i+1}:"))
    arr.append(ele)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
           temp=arr[i]
           arr[i]=arr[j]
           arr[j]=temp
for i in range(n):
    print(arr[i])