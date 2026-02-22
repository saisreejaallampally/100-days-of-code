n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    ele=int(input(f"Enter element {i+1}:"))
    arr.append(ele)
k=int(input("Enter the value of k:"))

for i in range(n):
    if arr[i]==k:
        print(f"found at index {i}")
        break
else:
    print("not found")