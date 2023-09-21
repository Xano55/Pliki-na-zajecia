'''
Typ sekwencyjny krotki - immutable!
TUPLA
DUPLA
'''
# moja_dupla = (3,4,5)
# print(type(moja_dupla))
# print(moja_dupla)

# moja_dupla2 = moja_dupla
# print(moja_dupla)

# lista = list(moja_dupla)
# lista.append(8)
# moja_dupla = tuple(lista)
# print(moja_dupla)

moja_dupla = (3,4,5)
moja_dupla = moja_dupla + (8,)
print(moja_dupla)

x, y, _ = 3, 4, 7
print(f"x= {x}, y = {y}")
x, y = y, x
print(f"x= {x}, y = {y}")

# w C++:
# int x = 3
# int y = 4

# int temp = x
# x = y
# y = temp