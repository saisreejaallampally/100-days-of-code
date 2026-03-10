word = input("Enter the word: ")
for char in word:
    count = 0
    for ch in word:
        if ch == char:
            count += 1
    if count == 1:
        print(char)
        break