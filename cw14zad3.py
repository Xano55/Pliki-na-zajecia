'''
wykres funkcji kwadratowej
'''

def wprowadzenie():
    while True:
        try:
            a = float(input("Podaj a = "))
            b = float(input("Podaj b = "))
            c = float(input("Podaj c = "))
            return a,b,c
        except ValueError:
            print("Podana wartosc jest niepoprawna")



def main():
    print("Aplikacja do kreslenia funkcji kwadratowej")
    a, b, c = wprowadzenie()
    print(f"Podales liczby a={a}, b={b}, c={c}")    
if __name__ = "__main__":
    main()