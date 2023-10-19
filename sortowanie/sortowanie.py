'''
Metody sortownia
K>K 2023
v. 1.0
'''
import random as rd
 
#funkcja wyswietlajaca menu
def menu():
    print(
        '''
        MENU
        b - bubble sort,
        i - inser sort,
        s - selection sort,
        q - quick sort  
        '''
    )
    
def pomiarczasu():
    pass
#bubble sort
def bubblesort(numbers):
    for i in range(len(numbers)):
        min_i = i
        for j in range(len(numbers)-1):
            if numbers[min_i] > numbers[j]:
                min_i = j
            numbers[min_i], numbers[i] = numbers[i], numbers[min_i]
            print(numbers, "\n")
    return numbers;
#insert sort
def insertsort(numbers):
    for i in range(1,len(n)):
        j = i
        while numbers[j] < numbers[j-1] and j > 0:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            j -= 1
    return numbers
#selection sort
def selectionsort():
    pass
#quicksort
def quicksort():
    pass
def pobierz():
    pass
def generator():
    print("===== Generowanie Liczb =====")
    n = int(input("Podaj ilość liczb do wygenerowania"))
    while n == 0:
        print("podales 0 bezmozgu")
        n = int(input("Podaj ilość liczb do wygenerowania"))
    d = int(input("Podaj dolny zakres liczb"))
    g = int(input("Podaj gorny zakres liczb"))
    if d > g: g = g, d
    nums = [rd.randint(d, g) for i in range(n)]
    return nums

def show(numbers, jakie = True):
    if jakie == True:
        print(f"\nLiczby przed sortowaniem to:")
        print(numbers)
    else:
        print(f"\nPosortowane liczby to:")
        print(numbers)
        
def witaj():
    print("\n")
    print("=" * 50)
    print("Sortowanie liczb")
    print("=" * 50)

#glowna funkcja aplikacji
def main():
    czygen = True
    witaj()
    while True:
        if czygen == True:
            numbers_g = generator()
        menu()
        wybor = input("Wybierz metode sortowania: ")
        if wybor in ('b', 'i', 's', 'q'):
            possort = [], 
            if wybor == 'b':
                liczby = numbers_g.copy()
                show(liczby, True)
                posort = bubblesort(liczby)
                show(possort, False)
            elif wybor == 'i':
                liczby = numbers_g.copy()
                show(liczby, True)
                posort = insertsort(liczby)
                show(possort, False)
            elif wybor == 's':
                liczby = numbers_g.copy()
                show(liczby, True)
                posort = selectionsort(liczby)
                show(possort, False)
            elif wybor == 'q':
                liczby = numbers_g.copy()
                show(liczby, True)
                posort = quicksort(liczby)
                show(possort, False)
            else:
                print("Niepoprawny wybor")
        menu()
    
        
        wyb = input("Czy chcesz kontynuowac? (t/n): ")
        if wyb in ('t', 'T', 'n', 'N'):
            if wyb != 't' and wyb != 'T':
                print("Spierdalaj")
                break
        else:
            wyb = input("Czy chcesz wygenerowac nowe liczby? (t/n): ")
            if wyb in ('t', 'T', 'n', 'N'):
                if wyb == 't' or wyb == 'T':
                    czygen = True
                else:
                    print("Wybierz")
            
                
  
#============================    
main()