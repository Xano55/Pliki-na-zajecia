#Liczenie liter
#Napisz funkcje, ktora przyjmuje ciag znakow i zwraca liczbe liter (ignorujac cyfry i znaki specjalne)

def stats(tekst):
    ilosc = {'litery':0, 'liczby':0, 'spacje':0, 'wyrazy':0}
    for litera in tekst:
        if litera.isalpha():
            ilosc["litery"] += 1
        elif litera == " ":
            ilosc["spacje"] += 1
        elif litera.isnumeric():
            ilosc["liczby"] += 1
            
    wyrazy = tekst.split()
    for i in wyrazy:
        ilosc["wyrazy"] += 1
    return ilosc


tekst = input("Podaj tekst: ")
print(f"Liczba liter w tekscie to {stats(tekst)}")
