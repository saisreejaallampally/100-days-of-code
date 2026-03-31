List=["flower","flow","float"]
substring=""
for i in range(len(List[0])):
    for word in List:
        if i>=len(word) or word[i]!=List[0][i]:
            print(substring)
            exit()
    substring+=List[0][i]
print(substring)