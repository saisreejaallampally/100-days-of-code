word=input("Enter the word:")
vowels=0
for ch in word:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        vowels+=1
print(f"there are {vowels} vowels in {word}")
print(f"there are {len(word)-vowels} consonants")