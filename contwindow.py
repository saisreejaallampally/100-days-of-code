# 333
# hjl
# arr=[-1,5,6,-3,-6,10,12]
# k=4
# n=len(arr)
# l=0
# r=k-1
# sum=sum(arr[:k])
# max_sum=sum
# while(r<n-1):
#     sum=sum-arr[l]
#     l+=1
#     r+=1
#     sum=sum+arr[r]
#     max_sum=max(sum,max_sum)
# print(max_sum)

arr=[-1,5,20,6,-3,-6,10,12]
k=4
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    max_sum=max(window_sum,max_sum)
print(max_sum)
