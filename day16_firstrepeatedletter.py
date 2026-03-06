word = input("Enter the word: ")
seen = ""
for ch in word:
    if ch in seen: 
        print(ch) 
        break       
    else:
        seen = seen + ch