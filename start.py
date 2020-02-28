# git-scm.com przydatne
# pep8 pep0008 
# Guido van Rossum
# dluga_nazwa_funkcji  (tak piszemy długie nazwy funkcji)
# print("Hello world!") szybkie komentowanie/odkomentowanie Ctrl+/
 
def main():
    print("Hello world!")

# Łańcuch znaków
# Shift + Alt + strzałka w dół/góre szybkie powielanie 

imie = 'Ala'
imie = "Ala"
imie = """Ala ma
kota a 
kot jest głodny""" #!!!!!!często urzywany do dokumentowania czyli docstring
imie =str("Ala") #poprzez konstruktor
print(type(imie))
print(type(5))
print(type(5.6))
print(type(True))
print(type(None))

#isinstance() sprawdzam czy zmienna jest danego typu 
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

print("Ala "+"ma kota.")
#print("Ala "+"ma "+ 5 + "kota.")
print("Ala "+"ma "+ str(5) + " kotów.")
ilosc_kotow = 5
print("Ala "+"ma {} kotów.".format(ilosc_kotow))
print("Ala" +  f"ma {ilosc_kotow} kotów.")
print("Ala" + "ma {1} {0} {2} kotów.".format(4, 5, 7))
liczba = 6.8721345
print(f"Liczba {liczba:.2f}") #dwa miejsca dziesiétne
#http://pyformat.info

print(imie[0])
#imie[0] = "o" nie jest mutowalny
imie = imie.lower()
print(imie)


# liczby!!!!!!!!!!!!!!


liczba = 1
liczbaf = 4.5
suma = liczba + liczbaf
print(1 + 2)
print(1 - 2)
print(1 / 2)
print(1 * 2)
print(1 // 2) #dzielenie bez reszty 
print(1 ** 2) #potęgowanie 
print(1 % 2) #modulo

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.30f}")


# listy!!!!!!!

