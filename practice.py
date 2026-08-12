"""n=int(input("enter n:"))
sum=0
for i in range(n+1):
    sum+=i
print(sum)"""
"""strng=input("Enter:")
count=0
for i in strng:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print(count)
strng=input("Enter:")
print(:strng)"""
"""s="dictionary"
vowels=0
consonants=0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1
print(vowels)
print(consonants)"""
"""s="sreeja"
print(s[::-1])
print(s[1:])
print(s[:-2])"""
"""s="python"
rev=""
for i in range (len(s)-1,-1,-1):
    rev+=s[i]
print(rev)"""
"""n=int(input("Enter the number:"))
lst=[]
for i in range(n):
    val=int(input("Enter:"))
    lst.append(val)
max=lst[0]
for i in range(n):
    if lst[i]>max:
        max=lst[i]
print(max)"""
"""lst=[5,4,6,9,9,2]
new_lst=[]
for ele in lst:
    if ele not in new_lst:
        new_lst.append(ele)
print(new_lst)"""
"""lst=[5,3,7,6,1]
max=lst[0]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
for i in range(len(lst)):
    print(lst[i])"""
"""lst=[6,3,7,5,1]
max=lst[0]
sec_max=lst[0]
for ele in lst:
    if ele>max:
        sec_max=max
        max=ele
    elif ele>sec_max and ele!=max:
        sec_max=ele
print(sec_max)"""
"""def sum_of_num(n):
    sum=0
    while n>0:
        rem=n%10
        sum+=rem
        n=n//10
    return sum
print(sum_of_num(12345))
sq=0
for i in range(5):
    sq=sq+5
print(sq)
"""
"""n=int(input("Enter n value:"))
sum=0
for i in range(n+1):
    sum+=i*i
print(sum)"""
"""print("Find the missing value")
actual_lst=[1,2,4,5]
actual_sum=1+2+4+5
sum=0
for i in range(5+1):
    sum+=i
missing_val=sum-actual_sum
print(missing_val)"""


"""n=int(input("Enter n:"))

for num in range(2,n+1):
   count=0
   for j in range(1,n):
       if num%j==0:
           count+=1
   if count==2:
       print(num)"""
"""for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)"""
"""n=int(input("Enter:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")
s="varun sai"
length=0
for ch in s:
    if ch.isalpha():
       length+=1
print(length)"""
"""n=5
fact=1
for i in range(1,n+1):
   fact*=i
print(fact)"""
"""def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
print(fact(5))"""
"""s="varun"
rev=""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)"""
"""lst=[2,6,7,5,1]
max=lst[0]
for i in range(len(lst)):
    if lst[i]>max:
        max=lst[i]
lst.remove(max)
max=lst[0]
for i in lst:
    if i>max:
        max=i
print(max)
l=[2,2,3,3,4,4]
l1=list(set(l))
print(l1)
s={1,2,3}
s1={4,5,6}
print(str('v'6))
print(s==s1)
lst1=[2,3,4]
lst2=[5,6,7]
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if i==j:
            print(lst1[i]+lst2[j],end=" ")"""
"""lst=[1,1,2,3,4,2,4]
visited=[]
for i in range(len(lst)):
    if lst[i] not in visited:
        count=0
        for j in range(len(lst)):
           if lst[i]==lst[j]:
              count+=1
              visited.append(lst[i])
        print(f"{lst[i]}:{count}",end=" ")"""
"""def freq_of_each_ele(lst):
  visited=[]
  for i in range(len(lst)):
    if lst[i] not in visited:
        count=0
        for j in range(len(lst)):
           if lst[i]==lst[j]:
              count+=1
              visited.append(lst[i])
        print(f"{lst[i]}:{count}",end=" ")
freq_of_each_ele([1,1,2,3,4,2,4])"""
"""lst=[1,2]
lst2=[1,2]
print(list(set(lst+lst2)))"""
"""lst=[2,0,7,0,1,3,0]
lst1=[]
lst2=[]
for i in lst:
    if i==0:
        lst1.append(i)
    else:
        lst2.append(i)
print(lst2+lst1)"""
# lst=[5,1,4,3,2,6]
# target=9
# start=0
# curr_sum=0
# for end in range(len(lst)):
#     curr_sum+=lst[end]
#     while curr_sum>target:
#         curr_sum-=lst[start]
#         start+=1
#     if curr_sum==target:
#         print(lst[start:end+1])

# lst=[5,3,7,4,6,8]
# k=3
# window_sum=sum(lst[:k])
# max_sum=window_sum
# for i in range(k,len(lst)):
#     window_sum=window_sum - lst[i-k]+lst[i]
#     max_sum=max(max_sum,window_sum)
# print(f"{max_sum}")

# lst=[5,3,7,4,6,8]
# k=3
# target=17
# window_sum=sum(lst[:k])
# if window_sum==target:
#     print(lst[:3])
# for i in range(k,len(lst)):
#     window_sum=window_sum-lst[i-k]+lst[i]
#     if window_sum==target:
#         print(lst[i-k+1:i+1])
     
# lst=[5,2,7,1,6,9]
# k=4
# window_sum=sum(lst[:k])
# print(window_sum//k)
# for i in range(k,len(lst)):
#     window_sum=window_sum-lst[i-k]+lst[i]
#     avg=window_sum//k
#     print(avg)

# lst=[4,-7,6,-2,-3,1]
# k=3
# start=0
# for i in range(k):
#     if lst[i-k+1:i+1]<0:
#         print(lst[i])
#         break
# for i in range(k,len(lst)):
#     if lst[i-k+1:i+1]<0:
#        print(lst[i])
#     start+=1
n=3
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
# n=3
# for i in range(n+1):
#     for j in range(i):
#         print(j+1,end="")
#     print()

# for i in range(1,5):
#     for j in range(i):
#         print(i,end="")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(64+j),end="")
#     print()
# def linear_serach(lst,key):
#     for i in range(len(lst)):
#         if lst[i]==key:
#             return i
#     return -1
# res=linear_serach(lst=[4,5,6,2,1,7],key=2)
# print(res)
# def linear_search(lst,key):
#     if key in lst:
#         return lst.index(key)
#     return -1
# res=linear_search(lst=[4,5,6,2,1,7],key=2)
# print(res)
# def binary_search(lst,key):
#     low=0
#     high=len(lst)-1
#     while(low<=high):
#         mid=(low+high)//2
#         if lst[mid]==key:
#             return mid
#         elif lst[mid]<key:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# lst=[4,5,6,2,1,7]
# key=2
# lst.sort()
# res=binary_search(lst,key)
# print(res)
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# arr=[5,8,3,1,7]
# print(bubble_sort(arr))

# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j 
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr
# arr=[5,8,3,4,9,7]
# res=selection_sort(arr)
# print(res)
                
# n=int(input("Enter:"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime")
# n=int(input(""))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")
# n=int(input(""))
# for i in range(1,n+1):
#     for j in range(2,i):
#          if i%j==0:
#             break
#     else:
#         print(i)
# n=int(input(""))
# for i in range(2,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i]
# n=int(input(""))
# a=0
# b=1

# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# s=['v','a','r','u','n']
# i=0
# j=len(s)-1
# for i in range(j):

"""n=int(input(""))
matrix=[]
for i in range(n):
    row=[]
    for j in range(n):
        ele=int(input("Enter the element:"))
        row.append(ele)
    matrix.append(row)
for i in matrix:
    print(i)"""

# arr=[1,-4,9,-1,5,6]
# k=3
# sum=sum(arr[:k])
# max_sum=sum
# l=0
# r=k
# while(r<len(arr)-1):
#     sum=sum-arr[l]
#     l+=1
#     sum=sum+arr[r]
#     r+=1
#     max_sum=max(sum,max_sum)
# print(max_sum)


# arr=[6,8,3,7,5,2]
# k=20
# n=len(arr)
# l=0
# r=0
# sum=0
# maxlength=0
# while(r<n):
#     sum+=arr[r]
#     if sum<=k:
#         maxlength=max(maxlength,r-l+1)
#     else:
#         sum-=arr[l]
#         l+=1
#     r+=1
# print(maxlength)
    
# arr=[6,8,3,7,5,2,20]
# k=20
# n=len(arr)
# l=0
# r=0
# sum=0
# maxlength=0
# while(r<n):
#     sum+=arr[r]
#     while(sum>k):
#         sum-=arr[l]
#         l+=1
#     maxlength=max(maxlength,r-l+1)
#     r+=1
# print(maxlength)

# arr=[6,2,3,4,7,2,1,7,1]
# r=len(arr)-1
# k=4
# lsum=sum(arr[:k])
# rsum=0
# maxsum=lsum
# for i in range(k-1,-1,-1):
#     lsum-=arr[i]
#     rsum+=arr[r]
#     sum=lsum+rsum
#     maxsum=max(sum,maxsum)
#     r-=1
# print(maxsum)

# arr=[1,2,3,4,5]
# k=3
# windsum=sum(arr[:k])
# maxsum=windsum
# for i in range (k,len(arr)):
#     windsum=windsum-arr[i-k]+arr[i]
#     maxsum=max(windsum,maxsum)
# print(maxsum)

# arr=[1,2,3,4,5]
# k=3
# l=0
# r=k-1
# sum=sum(arr[:k])
# maxsum=sum
# while(r<len(arr)-1):
#     sum=sum-arr[l]
#     l+=1
#     r+=1
#     sum=sum+arr[r]
#     maxsum=max(sum,maxsum)
# print(maxsum)

# arr=[12,-1,-7,8,-15,30]
# k=4
# negarr=[]
# wind=arr[:k]
# for i in wind:
#     if i<0:
#         negarr.append(i)
#         break
# for i in range(k,len(arr)):
#     wind.remove(arr[i-k])
#     wind.append(arr[i])
#     for i in wind:
#         if i<0:
#             negarr.append(i)
#             break
# print(negarr)

# s="aabcabcdd"
# n=len(s)
# l=0
# r=0
# visited=set()
# maxlen=0
# while (r<n):
#     if s[r] not in visited:
#         visited.add(s[r])
#         len=r-l+1
#         r+=1
#     else:
#         visited.remove(s[r])
#         l+=1
#     maxlen=max(len,maxlen)
# print(maxlen)

# arr=[2,3,1,2,4,3]
# n=len(arr)
# l=0
# r=0
# target=6
# sum=0
# minlen=float('inf')
# while(r<n):
#     sum+=arr[r]
#     while(sum>=target):
#        minlen=min(minlen,r-l+1)
#        sum-=arr[l]
#        l+=1
#     r+=1
# print(minlen)

# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# for i in range(6):
#     for j in range(1,6-i):
#         print(j,end="")
#     print()


# n=5
# for i in range(1,n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(2*(n-i)-1):
#         print("*",end="")
#     print()

# n=5
# for i in range(1,n):
#     for j in range(i):
#         print("*",end="")
#     for k in range(n-i-1):
#         print(" ",end="")
#     for l in range(n-i-1):
#         print(" ",end="")
#     for m in range(i):
#         print("*",end="")
#     print()

# n=5
# for i in range(1,5):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

# arr=[4,2,6,2,5,1,8,]
# n=len(arr)
# l=0
# r=0
# maxlen=0
# visited=set()
# while r<n:
#     if arr[r] not in visited:
#         visited.add(arr[r])
#         len=r-l+1
#         r+=1
#     else:
#         visited.remove(arr[r])
#         l+=1
#     maxlen=max(len,maxlen)
# print(maxlen)

# arr=[4,3,7,9,6,2,8]
# n=len(arr)
# target=16
# minlen=float('inf')
# l=0
# r=0
# sum=0
# while r<n:
#     sum+=arr[r]
#     while(sum>=target):
#         minlen=min(minlen,r-l+1)
#         sum-=arr[l]
#         l+=1
#     r+=1
# print(minlen)

# n=int(input())
# arr=[]
# for i in range(n):
#     val=int(input())
#     arr.append(val)
# max=arr[0]
# min=arr[0]
# for num in arr:
#     if num>max:
#         max=num
#     if num<min:
#         min=num
# print(max,min)

# n=int(input())
# arr=[]
# for i in range(n):
#     val=int(input())
#     arr.append(val)
# max=arr[0]
# secmax=arr[0]
# for num in arr:
#     if num>max:
#         secmax=max
#         max=num
#     elif num>secmax and num!=max:
#         secmax=num
# print(secmax)

# arr=[2,6,7,1,9]
# print(arr[::-1])

# arr=[1,2,3,4,5]
# revarr=[]
# for i in range(len(arr)-1,-1,-1):
#     print(list[arr[i]])

# arr=[2,8,6,3,4]
# for i in range(len(arr)):
#     for j in range(i):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]

# print(arr)

# lst=[1,2,3,6,1,2,4,8,3]
# seen=[]
# for num in lst:
#     if num not in seen:
#         seen.append(num)
# print(seen)

# lst=[1,2,3,6,1,2,4,8,3]
# seen=[]
# for i in lst:
#     if i not in seen:
#         count=0
#         for j in lst:
#             if i==j:
#                 count+=1
#                 seen.append(i)
#         print(i,":",count)


# n=int(input())
# num=input().split()
# for i in range(n):
#     num[i]=int(num[i])
# print(num)



# lst=[2,6,4,8,7,1,3]
# k=3
# window_sum=sum(lst[:k])
# max_sum=window_sum
# for i in range(k,len(lst)):
#     window_sum=window_sum-lst[i-k]+lst[i]
#     max_sum=max(max_sum,window_sum)
# print(max_sum)


# lst=[2,6,4,8,7,1,3]
# k=3
# l=0
# r=k-1
# window_sum=sum(lst[:k])
# max_sum=window_sum
# while(r<len(lst)-1):
#     window_sum=window_sum-lst[l]
#     l+=1
#     r+=1
#     window_sum=window_sum+lst[r]
#     max_sum=max(max_sum,window_sum)
# print(max_sum)


# lst=[2,6,4,8,7,1,3]
# k=3
# l=0
# r=k-1
# window_sum=sum(lst[:k])
# while(r<len(lst)-1):
#     window_sum=window_sum-lst[l]
#     l+=1
#     r+=1
#     window_sum=window_sum+lst[r]
    

# arr=[5,2,9,4,3,7]
# k=3
# i=0
# j=k-1
# window_sum=sum(arr[:k])
# max_sum=window_sum
# while j<len(arr)-1:
#     window_sum=window_sum-arr[i]
#     i+=1
#     j+=1
#     window_sum=window_sum+arr[j]
#     max_sum=max(max_sum,window_sum)
# print(max_sum)


# arr=[5,2,9,4,3,7]
# k=3
# i=0
# j=k-1
# window_sum=sum(arr[:k])
# max_sum=window_sum
# start=0
# while(j<len(arr)-1):
#     window_sum=window_sum-arr[i]
#     i+=1
#     j+=1
#     window_sum=window_sum+arr[j]
#     if window_sum>max_sum:
#         max_sum=window_sum
#         start=i
# print(max_sum)
# print(arr[start:start+k])


# arr=[2, 2, 2, 2, 5, 5, 5, 8]
# k=3
# i=0
# j=k-1
# target=4
# window_sum=sum(arr[:k])
# count=0
# start=0
# if window_sum/k>=target:
#     count+=1
#     print(arr[start:start+k])
# while(j<len(arr)-1):
#     window_sum=window_sum-arr[i]
#     i+=1
#     j+=1
#     window_sum=window_sum+arr[j]
#     if window_sum/k>=target:
#         count+=1
#         start=i
#         print(arr[start:start+k])
# print(count)


# s="abiudflaoidj"
# k=3
# i=0
# j=k-1
# count=0
# maxcount=count
# start=0
# for ch in s[:k]:
#     if ch in "aeiou":
#         count+=1
# while(j<len(s)-1):
#     if s[i] in "aeiou":
#         count-=1
#     i+=1
#     j+=1
#     if s[j] in "aeiou":
#         count+=1
#     if count>maxcount:
#         maxcount=count
#         start=i
# print(maxcount)
# print(s[start:start+k])



# s="abcabcbb"
# i=0
# j=0
# seen=set()
# max_length=0
# while j<len(s):
#     if s[j] not in seen:
#         seen.add(s[j])
#         max_length=max(max_length,j-i+1)
#         j+=1
#     else:
#         seen.remove(s[i])
#         i+=1
# print(max_length)

    

# arr=[1,2,3,1,1,1,4,5,1,1,1,1,4,2,1]
# i=0
# j=0
# max_length=0
# start=0
# while(j<len(arr)):
#     if arr[j]==1:
#         if j - i + 1 > max_length:
#            max_length = j - i + 1
#            start = i
#     else:
#         i=j+1
#     j+=1
# print(max_length)
# print(arr[start:start+max_length])



# arr=[2,3,1,2,4,3]
# target=7
# n=len(arr)
# l=0
# r=0
# sum=0
# min_len=999
# while(r<n):
#     sum=sum+arr[r]
#     while(sum>=target):
#         min_len=min(min_len,r-l+1)
#         sum=sum-arr[l]
#         l+=1
#     r+=1
# print(min_len)



# arr=[1,1,1,0,0,0,1,1,1,1,0]
# count=0
# max_length=0
# for num in arr:
#     if num==1:
#         count+=1
#     else:
#         count=0
#     max_length=max(max_length,count)
# print(max_length)
    

# arr=[1,1,1,0,0,0,1,1,1,1,0]
# k=2
# i=0
# zero_count=0
# ans=0
# for j in range(len(arr)):
#     if arr[j]==0:
#         zero_count+=1
#     while(zero_count>k):
#         if arr[i]==0:
#             zero_count-=1
#         i+=1
#     ans=max(ans,j-i+1)
# print(ans)



arr = [[1, 2], [3, 4], [5, 6]]
for i in range(len(arr)):
    print(arr[i][1])



















    
    




















    



    







