n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    
    ele=int(input(f"Enter element {i+1}:"))
    arr.append(ele)

for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
           min_index=j
    temp=arr[i]
    arr[i]=arr[min_index]
    arr[min_index]=temp
for i in range(n):
    print(arr[i])
        
        
        

        