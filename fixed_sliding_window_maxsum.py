lst=[5,2,3,4,9,1]
k=3
window_sum=sum(lst[:3])
max_sum=window_sum
for i in range(k,len(lst)):
    window_sum=window_sum-lst[i-k]+lst[i]
    max_sum=max(window_sum,max_sum)
print(max_sum)