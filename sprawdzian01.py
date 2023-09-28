'''
Sprawdzian 01 Liczby, listy, krotki
    Piotr Malinowski
    Klasa: 3TPM
    Data: 28.09.23
'''

#1
lista1 = [2, 4, 6, 'Anna', 'Zenon']
#2
print(f"Lista1 zawiera elementy: {lista1}")
#3
lista1.remove(4)
#4
lista1.append(99)
#5
lista2 = [100, 200, 300]
#6
lista1.extend(lista2)
#7
print(f"Lista1 i Lista2 zawieraja elementy: {lista1} {lista2}")
#8
lista2.reverse()
#9
print(f"Odwrocona Lista2 zawiera elementy: {lista2} ")
#10
lista4 = sorted(lista1[0:2])
lista3 = sorted(lista1[5:])
lista1 = lista4 + lista3
#11
print(f"Posortowana Lista1 zawiera elementy: {lista1} ")
#12
moja_tupla = ('A', 'B', 'C')
#13
nowa_tupla = ('D', )
moja_tupla = moja_tupla + nowa_tupla
#14
print(f"Tupla zawiera elementy: {moja_tupla} ")
#BONUS
p = int(input("Podaj poczatek listy: "))
k = int(input("Podaj koniec listy: "))
x = int
listaX = [x for x in range(p, k, 1)]
if x/2 == 0:
    listaX.pop(x)
print(f"Stworzona lista: {listaX} ")