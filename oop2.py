'''
Konto bankowe klasy i obiekty
'''

class Osoba:
    def __init__(self, imie, nazwisko, wiek, saldo):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.saldo = saldo
        
    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko} i mam {self.wiek} lat."
    
    def przelew(self, ilosc):
        if ilosc > 0:
            self.saldo += ilosc 
            
    def wyplac(self, ilosc):
        if ilosc > 0 and ilosc <= self.saldo:
            self.saldo -= ilosc
        else:
            print(f"Nie wystaraczajace saldo na koncie")
            
    def pokaz_konto(self):
        return f"Obecny stan konta: {self.saldo}PLN"

osoba1 = Osoba("Piotr", "Malinowski", 16, 0)
osoba1.pokaz_konto()
osoba1.przelew(1000)
osoba1.wyplac(500)
osoba1.pokaz_konto()
    
