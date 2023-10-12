'''
Cwiczenia z funkcji
'''

# Obliczanie sredniej arytmetyczenej:
# Napisz funkcje, ktora przyjmuje liste liczb i zwraca ich srednia arytmetyczna.

# def srednia(lista):
#     ilosc = len(lista)
#     suma = sum(liczby)
#     if ilosc == 0:
#         return 0
#     else:
#         return suma / ilosc

# liczby = [2,3,5,3,5]
# print(srednia(liczby))

def srednia2(*args):
    suma = 0
    ilosc = len(args)
    if ilosc == 0:
        return 0
    for i in args:
        suma += i
    return suma/ilosc

print(srednia2(3,5,8,5,3,6,2,1,7,5,89,5,7,52,56,3,6,57,13,6,4,23,53,33,3,2,1,7,6,3,6,2,99999999999))
