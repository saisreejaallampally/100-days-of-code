word=input("Enter the word:")
counted=""
for char in word:
    if char not in counted:
        count=0
        for ch in word:
            if ch==char:
                count+=1
        if count>1:
           print(char,":",count)
           counted+=char