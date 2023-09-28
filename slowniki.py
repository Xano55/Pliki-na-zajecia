'''
Dictionary
key : value
'''

dic = {'imie': 'Piotr', 'wiek':18, 'wzrost': 1.81}

print(type(dic))
print(f"Moj slownik to: {dic}")

print(f"Klucze: {dic.keys}")
print(f"Wartosci: {dic.values}")

# print(f"Wiek: {dic['wiek']}")
# print(f"Wiek: {dic.get('wiek')}")

print(f"Slownik: {dic.items()}")

for k, v in dic.items():
    print(f"{k} - {v}")
    
    
dic.pop('wiek')
print(dic)
dic["wiek"] = 18
print(dic)

wiek = dic['wiek']
wzrost = dic['wzrost']
dic.pop('wzrost')
dic.pop('wiek')
print(dic.items())
dic['wiek'] = wiek
dic['wzrost'] = wzrost
print(dic.items())

#Zamian wartsoci nie kluczy
#dic['wiek'] , dic['wzrost'] = dic['wzrost'] , dic['wiek']
#print(dic.items())

tup = ('miejscowosc', 'Chojnice')
print(tup)
dic[tup[0]] = tup[1]
print(dic)

dic = list(dic.items())
dic[1], dic[2] = dic[2], dic[1]
dic = dict(dic)
print(dic)