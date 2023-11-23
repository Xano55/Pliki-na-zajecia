'''
wykres funkcji kwadratowej
'''
from bokeh.plotting import figure, show
from bokeh.models import Title 
import math 

def wprowadzenie():      
    while True:
        try:
            a = float(input("Podaj a = "))
            b = float(input("Podaj b = "))
            c = float(input("Podaj c = "))
            poczatek = int(input("Podaj dolny zakres funkcji: "))
            koniec = int(input("Podaj gorny zakres funkcji: "))
            krok = float(input("Podaj krok: "))
            return a,b,c, poczatek, koniec, krok
        except ValueError:
            print("Podana wartosc jest niepoprawna")

def ob_delta(a,b,c):
    return b**2 - (4*a*c)

def wykres(a,b,c,delta,poczatek,koniec,krok):
    wykres = figure(title = "Wykres funkcji kwadratowej ", width = 800, height = 600, toolbar_location="above")
    if delta < 0:
        print("Brak rozwiazan rzeczywistych")
        wykres.add_layout(Title(text = "Wykres nie przecina osi OX", align = "center"), "below")
        x0 = float(-b/(2*2))
        y0 = float(a*(x0**2) + (b*x0) + c)
        if a < 0:
            wykres.circle([x0], [y0], size = 6, color ="pink", alpha = 0.5, legend_label = f"Max = {x0}")
        else:
            wykres.circle([x0], [y0], size = 6, color ="pink", alpha = 0.5, legend_label = f"Min = {x0}")
    elif delta == 0:
        x0 = float(-b/(2*a))         
        print(f"Jedno rozwiazenie x0={x0}")
        if a < 0:
            wykres.circle([x0], [y0], size = 6, color ="pink", alpha = 0.5, legend_label = f"Max = {x0}")
        else:
            wykres.circle([x0], [y0], size = 6, color ="pink", alpha = 0.5, legend_label = f"Min = {x0}")
    elif delta > 0:
        x1 = float((-b - math.sqrt(delta)) / (2*a))
        x2 = float((-b - math.sqrt(delta)) / (2*a))
        print(f"Dwa rozwiazania x1= {x1} oraz x2= {x2}")
        wykres.circle([x1], [0], size = 6, color = "blue", alpha = 0.5, legend_label = f"Miejsce zerowe x1={x1}")
        wykres.circle([x1], [0], size = 6, color = "blue", alpha = 0.5, legend_label = f"Miejsce zerowe x2={x2}")
        x0 = float(-b/(2*2))
        y0 = float(a*(x0**2) + (b*x0) + c)
        if a < 0: 
            wykres.circle([x0], [y0], size = 6, color ="pink", alpha = 0.5, legend_label = f"Max = {x0}")
        else:
            wykres.circle([x0], [y0], size = 6, color ="pink", alpha = 0.5, legend_label = f"Min = {x0}")

    x = poczatek
    while x <= koniec:      
        y = float(a*(x**2) + (b*x) + c)
        wykres.circle([x], [y], size = 3, color = "blue", alpha = 0.5)
        x += krok
    show(wykres)
    
def main():
    print("Aplikacja do kreslenia funkcji kwadratowej")
    a, b, c, poczatek, koniec, krok = wprowadzenie()
    print(f"Podales liczby a={a}, b={b}, c={c}")    
    delta = ob_delta(a,b,c)
    print(f"Delta wynosi: {delta}")
    wykres(a,b,c,delta,poczatek,koniec,krok)
    
if __name__ == "__main__":
    main() 