'''
Cwiczenie 14
'''
from datetime import datetime
import math

#=========Zadanie1=========#

def dataur():
    while True:
        try:
            data = input("Podaj date urodzin (YYYY-MM-DD)")
            data = datetime.strptime(data, "%Y-%m-%d")
            return data
        except ValueError:
            print("Bledny lub niewlasciwy format daty!")

def najurodziny(data):
    localtime = datetime.now()
    urodziny = datetime(localtime.year, data.month, data.day)
    if localtime > urodziny:
        nadurodziny = datetime(localtime.year + 1, localtime.month, localtime.day)
    else:
        nadurodziny = urodziny
    liczbadni = (nadurodziny - localtime).days
    
    return nadurodziny, liczbadni
def main():
    print("Program obliczajacy czas do nastepnych urodzin!")
    data = dataur
    print(f"Twoje urodziny były dnia: {data}")
    najblizszeurodziny, liczbadni = najurodziny(data)
    
    print(f"Najblizsze urodziny:" ,{najurodziny.strftime("%Y-%m-%d")})
    print(f"Liczba dni do najblizszych urodziny: {liczbadni}")
    
if __name__ == "__main__":
    main()

dataur()

