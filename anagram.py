wyrazenie1 = input("Podaj słowo: ").lower().replace(" ","")
wyrazenie2 = input("Podaj słowo: ").lower().replace(" ","")
print(wyrazenie1)
print(wyrazenie2)

wyrazenie1Sorted = sorted(wyrazenie1)
wyrazenie2Sorted = sorted(wyrazenie2)

if wyrazenie1Sorted == wyrazenie2Sorted:
    print("Anagram")
else:
    print("Nie anagram")
