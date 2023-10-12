'''
Funckje w python
'''

def menu():
    print(f"Wybor: d - dodawanie, o - odejmowanie, m - mnozenie, s - dzielenie")
    
def kalkulator(dzialanie, a, b):
    if dzialanie == "d":
        return a + b
    elif dzialanie == "o":
        return a - b
    elif dzialanie == "m":
        return a * b
    elif dzialanie == "s": 
        if b != 0:
            return a / b
        else:
            return "Nie moge podzielic przez 0"
    else:
        return "Zly wybor dzialania"    
    
def f_main():
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    menu()
    dzialanie = input()
    print(f"Wynikiem dzialania  {dzialanie}  dla liczb  {a} i {b} jest {kalkulator(dzialanie, a, b)}") 
    
f_main()