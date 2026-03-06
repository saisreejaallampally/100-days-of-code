word = input("Enter the word: ")
seen = ""
printed=""
for ch in word:
    if ch in seen:
        if ch not in printed:
        
           print(ch)
           printed=printed+ch        
    else:
        seen = seen + ch