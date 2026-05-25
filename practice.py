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




















    



    







