word=input("Enter the word:")
repeated=""
for char in word:
    if char not in repeated:
        repeated+=char
print(repeated)