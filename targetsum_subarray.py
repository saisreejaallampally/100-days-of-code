lst=[2,6,7,3,4]
target=10
curr_sum=0
start=0
for end in range(len(lst)):
    curr_sum+=lst[end]
    while curr_sum>target:
        curr_sum-=lst[start]
        start+=1
    if curr_sum==target:
        print(lst[start:end+1])

