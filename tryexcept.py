'''
Obsluga bledow try i except
'''

try:
    x = int(input("Podaj liczbe: "))
    wynik = 10 / x
    print("Wynik: ", wynik)
except ZeroDivisionError:
    print("Nie można dzielic przez zero!")
except ValueError:
    print("Podana liczba nie jest liczbą calkowita!")
except Exception as e:
    print("Wystapil wyjatek: " + e)
finally:
    print("Zabij sie💀")