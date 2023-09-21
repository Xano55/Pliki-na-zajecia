'''
Porwonanie petli i list comprehension
'''
import random as rd
#from random import randint as rdi
liczby = []
for i in range(1000):
    liczby.append(rd.randint(1,100))

print(liczby)

#list comprehension

liczby_losowe = [ rd.randint(1,100) for i in range(1000) ]
print(liczby_losowe)

#Zbuduj liste 100 liczb rzeczywistych z zakresu 0 do 1

lista = [rd.uniform(0,1) for x in range(100)]

print(lista)