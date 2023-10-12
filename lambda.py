'''
Lambdy 😂😂😂
🧑🏻🧑🏻🧑🏻
🚽🚽🚽
'''

# kwadrat = lambda x: x ** 2
# print(kwadrat(5))

# liczby = [1,2,3,4,5]
# parzyste = list(map(lambda x: x % 2 == 0, liczby))
# print(parzyste)

# slowa = ["japko", "banan", "tryskawka", "maliniarz", "kantalopa", "lotermelon", "gayfruit"]
# slowa_sorted = sorted(slowa, key=lambda x: len(x))
# print(slowa_sorted)

# dane = [(1,5), (3,2), (2,8), (4,1)]
# dane_sorted = sorted(dane, key=lambda x: x[1])
# print(dane_sorted)

# slowa = ["japko", "banan", "tryskawka", "maliniarz", "kantalopa", "lotermelon", "gayfruit"]
# litera = "m"
# slowa_filtr = list(filter(lambda x: x.startswith(litera), slowa))
# print(slowa_filtr)

#Tworzenie listy z trojkatow o roznych polach, uzywajac lambda:

boki = [3,4,5]
wysokosci = [4,5,6]

pole = list(map(lambda a, b: 0.5 * a * b, boki, wysokosci))
print(pole)