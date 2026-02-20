n=int(input("Enter the size:"))
arr=[]
for i in range(n):
    ele=int(input(f"Enter element {i+1}:"))
    arr.append(ele)
i=0
j=n-1
flag=True
while i<j:
    if arr[i]!=arr[j]:
        flag=False
        break
    i=i+1
    j=j-1
if flag:
    print("palindrome")
else:
    print("no")