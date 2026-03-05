word=input("Enter the word:")
rev_word=""
for i in range(len(word)-1,-1,-1):
    rev_word=rev_word+word[i]
print(rev_word)
#using slicing
print(word[::-1])