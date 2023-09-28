'''
Sets - zbiory
'''

zb = {2, 5, 1, 3, 5, 1}
print(zb)

#zb1 = set()
#print(zb1)

zb.add(4)
zb.add(5)
print(zb)

#zb.remove(2) bedzie blad jesli nie ma elemntu

#zb.discard(2) nie bedzie bledu nawet jesli nie ma elemntu

a = {1, 3, 5}
b = {2, 3, 6}

# wspolna = a.intersection(b)
# print(wspolna)

# suma = a.union(b)
# print(suma)

# roznica = a.difference(b)
# print(roznica)

# roznica2 = b.difference(a)
# print(roznica2)

if 3 in b:
    b.remove(3)
    
if 3 in b:
    b.remove(3)
    
print(b)

# lista1 = [2,4,5,6,9]
# if 5 in lista1:
#     print("Jest😱😱😱")
# else:
#     print("slepy jestes")
    
listaX = [2,3,4,2,3,4,2,3,4]

#usun z listy elementy powtarzajace sie
listaX = list(set(listaX))
print(listaX)