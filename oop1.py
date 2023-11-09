'''
Klasy i obiekty
'''

class Osoba:
    def __init__(self, imie, nazwisko, wiek = 16):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko} i mam {self.wiek} lat."
    def zwieksz_wiek(self, ile = 0):
        self.wiek += ile 
        return self.wiek

class Uczen(Osoba):
    def __init__(self, imie, nazwisko, wiek, klasa):
        super().__init__(imie, nazwisko, wiek)
        self.klasa = klasa
    def przedstaw_sie(self):
        return f"Jestem uczniem mam {self.wiek} lat, nazywam sie {self.imie} {self.nazwisko} i chodze do klasy {self.klasa}"
        
class Nauczyciel(Osoba):
    def __init__(self, imie, nazwisko, wiek, przedmiot):
        super().__init__(imie, nazwisko, wiek)
        self.przedmiot = przedmiot
        self.wyplata = 1
    def przedstaw_sie(self):
        return f"Jestem nauczycielem {self.przedmiot}, nazywam sie {self.imie} {self.nazwisko} i mam {self.wiek} lat"
    def zwieksz(self, kwota):
        self.wyplata += kwota
        return self.wyplata
    def pokarz_wyplate(self):
        return f"Obecna wypłata to {self.wyplata}"
def przywitanie(osoby):
    return osoby.przedstaw_sie()
def main():
    osoba1 = Osoba("Gigachad", "Sigmowski", 35)         
    print(osoba1.przedstaw_sie())
    
    nauczyciel1 = Nauczyciel("Janusz", "Laska", 80, "Histori")     
    print(nauczyciel1.przedstaw_sie())
    nauczyciel1.zwieksz(2000)
    nauczyciel1.pokarz_wyplate()    
    uczen1 = Uczen("Piotr", "Malinowski", 16, "3TPM")         
    print(uczen1.przedstaw_sie())
                  
main()
