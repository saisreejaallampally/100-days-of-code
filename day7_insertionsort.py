n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    ele=int(input(f"Enter element {i+1}:"))
    arr.append(ele)
for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1   
    arr[j+1]=key
for i in range(n):
    print(arr[i])