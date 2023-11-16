'''
Histogram
'''

import random
import math
import matplotlib.pyplot as plt


def sposob1(liczby):
    zakresy = [ -10, -5, 0, 5, 10 ]
    plt.hist(liczby, bins = zakresy, color="white", ec="white")
    plt.title(f"Histogram z liczb rzeczywistych w zakresie {zakresy}")
    plt.xlabel("liczby")
    plt.ylabel("Ilosc liczb")
    plt.xticks(zakresy)
    plt.show()
    
def generator(n, d, g):
    if d>g: d,g = g,d
    return [ random.randint(d,g) for i in range(n) ]


def main():
    liczby = generator(100, -10, 10)
    print(f"Liczby to: {liczby}")
    sposob1(liczby)
if __name__ == "__main__":
    main()