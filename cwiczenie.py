'''
Piotr Malinowski
Zadanie Domowe z Obiektow i Klas
'''
#-*- coding: utf-8 -*-

class Samochod:
    def __init__(self, marka, model, rocznik, p_silnika, przebieg, wlasciciel):
        self.model = model
        self.marka = marka
        self.rocznik = rocznik
        self.p_silnika = p_silnika
        self.przebieg = przebieg
        self.wlasciciel = wlasciciel
    def pokarz_samochod(self):
        return f"Samochod to {self.marka}, model {self.model}, rocznik {self.rocznik}, pojemnosc silnika wynosi {self.p_silnika}, przebieg {self.przebieg} i nalezy ono do {self.wlasciciel}"
    def zmien_przebieg(self, zmien = 0):
        self.przebieg += zmien
        return self.przebieg
    def zmien_wlasciciela(self, wlasciciel):
        pass
    def zapisz_samochod(self):
        with open("pojazdy.txt", "a") as poj:
            poj.write(f"Marka {self.marka}, Model: {self.model}, Rocznik: {self.rocznik}, Pojemnosc silnika: {self.p_silnika}, Przebieg: {self.przebieg}, Wlasciciel: {self.wlasciciel}")
class Osobowy(Samochod):
    def __init__(self, marka, model, rocznik, p_silnika, przebieg, wlasciciel, li_miejsc):
        super().__init__(marka, model, rocznik, p_silnika, przebieg, wlasciciel)
        self.li_miejsc = li_miejsc
    def pokarz_samochod(self):
        return f"Samochod osobowy to {self.marka}, model {self.model}, rocznik {self.rocznik}, pojemnosc silnika wynosi {self.p_silnika}, przebieg {self.przebieg}, posiada {self.li_miejsc} miejsc i nalezy ono do {self.wlasciciel}"
    def zmien_li_miejsc(self, miejsca = 0):
        self.li_miejsc += miejsca
        return self.li_miejsc
    
auto1 = Samochod("BMW", "9.1", 2001, 50, 200, "Piotr")
print(auto1.pokarz_samochod())
auto1.zmien_przebieg(20)
print(auto1.pokarz_samochod())