'''
Wygeneruj 1000 slow z losowych liter o dlugosciach od 3 do 10 znakow i zapisz je do pliku w kolejnych liniach
'''
import random

with open("losowytext.txt", "wt") as f:
    for i in range(1000):
        dl = random.randint(3,10)
        wyraz = ''
        for j in range(dl):
            wyraz += chr(random.randint(97,122))
        f.write(f"{wyraz}\n")
        
with open("losowytext.txt", "r") as f:
    wyrazy = f.readlines()
    for i in range(len(wyrazy)):
        wyrazy[i] = wyrazy[i].replace("\n", "")
        if len(wyrazy[i]) > 4 and wyrazy[i] == wyrazy[i][::-1]:
            print(wyrazy[i])