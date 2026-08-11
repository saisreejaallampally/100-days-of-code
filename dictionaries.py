# d={
#     "name":"sreeja",
#     "age":20
# }
# print(d)


# d={}
# n=int(input())
# for i in range(n):
#     key=input("key:")
#     value=input("value:")
#     d[key]=value
# print(d)


# d={}
# n=int(input())
# for i in range(n):
#     key=input("key:")
#     value=input("value:")
#     d[key]=value
# for value in d.values():
#     print(value)


# d={}
# n=int(input())
# for i in range(n):
#     key=input("key:")
#     value=input("value:")
#     d[key]=value
# for i,j in d.items():
#     print(i,j) 


# d={}
# n=int(input())
# for i in range(n):
#     key=input("key:")
#     value=input("value:")
#     d[key]=value
# d["address"]="wana"
# print(d)


# d={}
# n=int(input())
# for i in range(n):
#     key=input("key:")
#     value=input("value:")
#     d[key]=value
# d["age"]=21
# print(d)


# d={}
# n=int(input())
# for i in range(n):
#     key=input("key:")
#     value=input("value:")
#     d[key]=value
# del d["place"]
# print(d)



# arr=[2,5,3,9,3,5,7,4,7]
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# s="mississippi"
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# s="how much wood would a wood chuck chuck if a wood chuck would chuck wood".split()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# n=int(input())
# d={}
# for i in range(n):
#     key=input("key:")
#     value=input("value:")
#     d[key]=value
# key="age"
# if key in d:
#     print("yes")
# else:
#     print("no")


# d = {1:50, 2:80, 3:40, 4:90}
# max=d[1]
# for i in d:
#     if d[i]>max:
#         max=d[i]
# print(max)
    

# d={1:60,2:70,3:45,4:52}
# min=d[1]
# for i in d:
#     if d[i]<min:
#         min=d[i]
# print(min)


# d={5:3,7:8,1:6,9:5}
# max_key=list(d.keys())[0]
# for i in d:
#     if i>max_key:
#         max_key=i
# print(max_key)


# arr=[2,5,6,4,2,5,8,9,6]
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# count=0
# for i in d:
#     if d[i]==1:
#         count+=1
# print(count)


# arr=[2,5,6,4,2,5,8,9,6]
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for key,value in d.items():
#     if value==1:
#         print(key,value)


# arr=[2,5,6,4,2,5,8,9,6]
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for key,value in d.items():
#     if value>1:
#         print(key)


# arr=[2,5,6,4,2,5,8,9,6]
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for key,value in d.items():
#     if value==1:
#         print(key)


# arr=[2,5,6,4,2,5,8,9,6]
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for key,value in d.items():
#     if value==1:
#         print(key)
#         break



# lst=list(map(int,input().split()))
# d={}
# max=lst[0]
# for key in lst:
#     if key 


# d={
#     "banana":30,
#     "apple":50,
#     "mango":20
# }
# d["banana"]=35
# print(d)


# d = {"A": 10, "B": 20, "C": 30}
# d["D"]=40
# d["B"]=50
# del d["A"]
# print(d)


# arr=[1,2,3,4,3,2,1]
# d={}
# for num in arr:
#     if num in d:
#         d[num]+=1
#     else:
#         d[num]=1
# print(d)


# arr=[1,2,3,4,3,2,1,3,3]
# d={}
# max=0
# ans=0
# for num in arr:
#     if num in d:
#         d[num]+=1
#     else:
#         d[num]=1
#     if d[num]>max:
#         max=d[num]
#         ans=num
# print(max)
# print(ans)


# arr=[1,2,3,4,3,2,1,3,3]
# d={}
# max=0
# ans=0
# for num in arr:
#     if num in d:
#         d[num]+=1
#     else:
#         d[num]=1
#     if d[num]>max:
#         max=d[num]
#         ans=num
# print(ans,":",max)


# arr = [1, 2, 3, 2, 4, 2, 5]
# d={}
# for num in arr:
#     if num in d:
#         d[num]+=1
#     else:
#         d[num]=1
#     if d[num]==3:
#         print(num)


# arr = [1, 2, 3, 2, 4, 2, 5, 3, 3]
# d={}
# for num in arr:
#     if num in d:
#         d[num]+=1
#     else:
#         d[num]=1
# for key in d:
#     if d[key]==3:
#         print(key)


arr=[4, 5, 1, 2, 1, 5, 4, 6]
d={}
for num in arr:
    if num in d:
        d[num]+=1
    else:
        d[num]=1
for num in arr:
    if d[num]==1:
        print(num)
        break