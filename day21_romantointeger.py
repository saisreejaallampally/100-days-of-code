roman=input("Enter the roman number:")
rom_val={
    'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
}
total=0
for i in range(len(roman)):
    if i<len(roman)-1 and rom_val[roman[i]]<rom_val[roman[i+1]]:
        total=total-rom_val[roman[i]]
    else:
        total=total+rom_val[roman[i]]
print(total)

