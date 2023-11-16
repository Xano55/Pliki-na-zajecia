#===================Zadanie 1==================# 
'''
Piotr Malinowski
3TPM
26.10.2023
'''

#===================Zadanie 2==================# 
import random as rd;

liczby = [rd.randint (1, 100) for i in range (1000)]
try:
    with open("liczby.txt", "w") as liczba:
        for i in range(100):
            liczba.write(f"{rd.randint(1, 100)}\n")
except FileNotFoundError:
    print("Nie znaleziono pliku")
#===================Zadanie 3==================# 
suma = 0
iloczyn = 1
minint = 0
maxint = 0
średnia = 0
ilosc = 0

try:
    with open("liczby.txt", "r") as odczyt:
        for i in odczyt.readlines():
            i = int(i)
        ilosc += 1
        średnia += suma / ilosc
        suma += i
        iloczyn *= i
        if (i > maxint):
            maxint = i
        elif (minint > i):
            minint = i
except FileNotFoundError:
    print("Nie znaleziono pliku")

def staty():
    print(f"Suma liczb wynosi: {suma}\n")
    print(f"Srednia liczb wynosi: {średnia}\n")
    print(f"Iloczyn liczb wynosi: {iloczyn}\n")
    print(f"Najwieksza liczba wynosi: {maxint}\n")
    print(f"Najmniejsza liczba wynosi: {minint}\n")
    return suma, średnia, iloczyn, maxint, minint

statystyki = {
    'suma': suma, 
    'srednia': średnia, 
    'iloczyn': iloczyn, 
    'maxint': maxint, 
    'minint': minint
    }

with open("staty.txt", "w") as stat:
    for k, v in statystyki.items():
        stat.write(f"{k} - {v} ")
print(staty())

#===================Zadanie 4==================#
with open("liczby.txt", "r") as wczyt:
    with open("kody.txt", "w") as kod:
        wczyt.read()
        i = int(i)
        linia = i
        for i in wczyt.readlines():
            if(i >= 65 and i <= 90) or (i >= 97 and i <= 122):
                i = chr(i)
                wczyt.write(f"{i} - {linia}")
        linia += i