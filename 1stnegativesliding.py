arr=[12,-1,-7,8,-15,30]
k=4
negwind=[]
wind=arr[:k]
for i in wind:
    if i<0:
        negwind.append(i)
        break
for i in range(k,len(arr)):
    wind.remove(arr[i-k])
    wind.append(arr[i])
    for i in wind:
        if i<0:
            negwind.append(i)
            break
print(negwind)
