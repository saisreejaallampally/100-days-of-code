# Find the length of a string without using len().
# Reverse a string without using slicing ([::-1]).
# Check whether a string is a palindrome.
# Count the number of vowels in a string.
# Count vowels and consonants separately.
# Convert lowercase letters to uppercase without using upper().
# Count the number of spaces in a string.
# Count the frequency of a particular character.
# Print each character of a string on a separate line.
# Find the first and last character of a string.


# s="sreeja"
# count=0
# for i in s:
#     count+=1
# print(count)

# s="sreeja"
# new_str=""
# for i in range(len(s)-1,-1,-1):
#     new_str+=s[i]
# print(new_str)

# s="sreeja"
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end="")

# s="sreeja"
# if(s==s[::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")

# s="sreeja"
# i=0
# j=len(s)-1
# while(i<j):
#     if s[i]!=s[j]:
#         print("not palindrome")
#         break
#     i+=1
#     j-=1
# else:
#     print("palindrome")

# s="sreeja"
# v_count=0
# for ch in s.lower():
#     if ch in "aeiou":
#         v_count+=1
# print(v_count)

# s="sreeja"
# v_count=0
# c_count=0
# for ch in s.lower():
#     if ch in "aeiou":
#         v_count+=1
#     elif ch.isalpha():
#         c_count+=1
# print(v_count)
# print(c_count)

# s="sreeja"
# new_str=""
# for ch in s:
#     if 'a'<=ch<='z':
#         new_str+=chr(ord(ch)-32)
#     else:
#         new_str+=ch
# print(new_str)
# print(s.upper())

# s="sai sreeja"
# count=0
# for ch in s:
#     if ch==" ":
#         count+=1
# print(count)
# print(s.count(" "))

# s="mississippi"
# count=0
# for ch in s:
#     if ch=='s':
#         count+=1
# print(count)

# s="sreeja"
# for ch in s:
#     print(ch)

# s="sreeja"
# print(s[0])
# print(s[-1])


# Count the frequency of every character in a string.
# Remove all spaces from a string.
# Remove duplicate characters from a string.
# Find the first non-repeating character.
# Find the first repeating character.
# Check whether two strings are anagrams.
# Count the number of words in a sentence.
# Find the longest word in a sentence.
# Replace all vowels with *.
# Find the most frequent character in a string.

# s="mississippi"
# d={}
# for ch in s:
#     if ch not in d:
#         d[ch]=1
#     else:
#         d[ch]+=1
# print(d)

# s="mississippi"
# n_s=""
# for ch in s:
#     if ch not in n_s:
#         n_s+=ch
#         count=0
#         for char in s:
#             if ch==char:
#                 count+=1
#         print(ch,":",count)

# s="i love python"
# new_s=""
# for ch in s:
#     if ch!=" ":
#         new_s+=ch
# print(new_s)

# s="i love python"
# print(s.replace(" ",""))


# s="i love python"
# new_s=s.split()
# print("".join(new_s))

# s="mississippi"
# n_s=set(s)
# print(str(n_s))

# s="mississippi"
# new_s=""
# for ch in s:
#     if ch not in new_s:
#         new_s+=ch
# print(new_s)

# s="mississppi"
# d={}
# for ch in s:
#     if ch not in d:
#         d[ch]=1
#         print(ch,end="")

# s="characteristics"
# new_s=""
# for ch in s:
#     if ch not in new_s:
#         new_s+=ch
#     else:
#         print(ch)
#         break

# s="characteristics"
# d={}
# for ch in s:
#     if ch not in d:
#         d[ch]=1
#     else:
#         print(ch)
#         break 

# s="characteristics"
# for i in s:
#     if s.count(i)==1:
#         print(i)
#         break

# s="characteristics"
# d={}
# for ch in s:
#     if ch not in d:
#         d[ch]=1
#     else:
#         d[ch]+=1
# for ch in s:
#     if d[ch]==1:
#         print(ch)
#         break

# s1="silent"
# s2="loud"
# if len(s1)!=len(s2):
#     print("no")
# else:
#     for i in s1:
#         if s1.count(i)!=s2.count(i):
#             print("no")
#             break
#     else:
#         print("anagrams")

# s="I am sai sreeja"
# new_s=s.split()
# count=0
# for i in new_s:
#     count+=1
# print(count)
# print(len(s.split()))

# s="i am learning python programming"
# new_s=s.split()
# max_len=0
# longest=""
# for i in new_s:
#     if len(i)>max:
#         max_len=len(i)
#         longest=i
# print(longest)

# s="sreeja"
# for ch in s:
#     if ch in "aeiou":
#         ch="*"
#     print(ch,end="")

# s="sreeja"
# new_s=""
# for ch in s:
#     if ch in "aeiou":
#         new_s+="*"
#     else:
#         new_s+=ch
# print(new_s)

# s="mississippi"
# d={}
# for ch in s:
#     if ch not in d:
#         d[ch]=1
#     else:
#         d[ch]+=1
# max_len=0
# letter=""
# for ch in s:
#     if d[ch]>max_len:
#         max_len=d[ch]
#         letter=ch
# print(letter)


# Reverse each word in a sentence.
# Reverse the order of words in a sentence.
# Find the longest common prefix among strings.
# Check whether a string contains only digits.
# Find all duplicate characters.
# Remove a particular character from a string.
# Find the second most frequent character.
# Check whether one string is a rotation of another.
# Compress a string (e.g., aaabbc → a3b2c1).
# Find the longest substring without repeating characters.


# s="i am learning python programming"
# new_s=s.split()
# for i in new_s:
#     print(i[::-1],end=" ")

# s=["clap","club","clove"]
# s.sort()
# first=s[0]
# last=s[-1]
# for i in range(len(first)):
#     if first[i]!=last[i]:
#         break
#     print(first[i],end="")

# s="123456"
# if s.isdigit():
#     print("only digits")
# else:
#     print("no")

# s="1234jsdg5"
# count=0
# for i in s:
#     if i>='0' and i<='9':
#         count+=1
# if len(s)==count:
#     print("yes")
# else:
#     print("no") 

# s="mississippi"
# d={}
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# for i in d:
#     if d[i]>1:
#         print(i)
        
# s="mississippi"
# n_s=""
# for ch in s:
#     if s.count(ch)>1 and ch not in n_s:
#         n_s+=ch
# print(n_s)

# s="mississippi"
# n_s=""
# for ch in s:
#     if ch!='s':
#         n_s+=ch
# print(n_s)

# s="sreeja"
# print(s.replace('s',""))

# s="sreeja"
# d={}
# for ch in s:
#     if ch not in d:
#         d[ch]=1
#     else:
#         d[ch]+=1
# max=0
# sec_max=0
# longest=""
# sec_longest=""
# for ch in d:
#     if d[ch]>max:
#         sec_max=max
#         sec_longest=longest
#         max=d[ch]
#         longest=ch
#     elif d[ch]>sec_max and d[ch]!=max:
#         sec_max=d[ch]
#         sec_longest=ch
# print(sec_longest)

# s="aaabbc"
# a_count=0
# b_count=0
# c_count=0
# for i in s:
#     if i=='a':
#         a_count+=1
#     elif i=='b':
#         b_count+=1
#     elif i=='c':
#         c_count+=1
# print('a'+str(a_count)+'b'+str(b_count)+'c'+str(c_count))

# s="aaabbc"
# visited=""
# for i in s:
#     count=0
#     if i not in visited:
#       visited+=i
#       for j in s:
#         if i==j:
#             count+=1
#       print(i+str(count),end="")
      
# lst=[1,2,3,4,5]
# n_lst=[]
# for i in lst:
#     n_lst.append(i)
# print(n_lst)

# lst=[4,6,4,2,6,5]
# n_lst=[]
# for i in lst:
#     if i not in n_lst:
#         n_lst.append(i)
# print(n_lst)

# lst=[4,6,4,2,6,5]
# n_lst=[]
# d={}
# for i in lst:
#     if i not in d:
#         d[i]=1
#         n_lst.append(i)
# print(n_lst)
    
# lst=[4,6,5,7,4,3,5]
# lst.sort()
# i=0
# for j in range(1,len(lst)):
#     if lst[i]!=lst[j]:
#         i+=1
#         lst[i]=lst[j]
# print(lst[:i+1])

# lst=[5,3,5,4,2,3]
# d={}
# for i in lst:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# for i in d:
#   if d[i]==1:
#       print(i)

# lst=[5,0,3,6,0,1,0,0,2]
# lst1=[]
# lst2=[]
# for i in lst:
#     if i!=0:
#         lst1.append(i)
#     else:
#         lst2.append(i)
# print(lst1+lst2)

# lst1=[1,2,3,4,5]
# lst2=[1,2,4,5]
# print(sum(lst1)-sum(lst2))

# lst=[5,0,3,6,0,1,0,0,2]
# i=0
# for j in range(len(lst)):
#     if lst[j]!=0:
#         lst[i],lst[j]=lst[j],lst[i]
#         i+=1
# print(lst)

