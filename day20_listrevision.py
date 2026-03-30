n=int(input("Enter the size of the list:"))
list=[]
dup_list=[]
for i in range(n):
    elements=int(input(f"Enter element no. {i+1}:"))
    list.append(elements)
print(list)
for i in range(n):
    if list[i] not in dup_list:
        dup_list.append(list[i])
print(dup_list)
