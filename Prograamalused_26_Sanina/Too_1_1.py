from ast import Try
from random import * #randint
from math import * #pi


#Ülesanne 1
print ("Tere, maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try:
    vanus=int(input("Sisesta ona vanus: "))
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun sisesta kehtiv number vanuse jaoks. ")


#Ülesanne 2
vanus=17 #int-täisarv
eesnimi="Anna" #str-sõne
pikkus=17.5 #float-kümnenmurd/ujukomaarv
kas_käib_koolis=True #bool-tõeväärtus
print(f"Vanus:{vanus}, tüüp:{type(vanus)}")
print(f"Eesnimi:{eesnimi}, tüüp:{type(eesnimi)}")
print(f"Pikkus:{pikkus}, tüüp:{type(pikkus)}")
print(f"Käib koolis:{kas_käib_koolis}, tüüp:{type(kas_käib_koolis)}")


#Ülesanne 3
kommide_arv=randint(1, 100)       #int(input("Kommide arv: "))
print(f"Laud on {kommide_arv} kommi.")
try: 
    kommid=int(input("Mitu kommi soovid ära võtta? "))
    kommide_arv -= kommid
    print(f"Laud on nüüd {kommide_arv} kommi. ")
except ValueError:
    print("Palun sisesta number.")


#Ülesanne 4
try:
    ümbermõõt=float(input("Sisesta puu ümbermõõt: "))
    läbimõõt=round(ümbermõõt/pi,1)
    print(f"Puu läbimõõt on {läbimõõt}.") 
except ValueError:
    print("Palun sisesta number.")


#Ülesanne 5
try:
    N=float(input("Sisesta ristküliku esimene külg (N): "))
    M=float(input("Sisesta ristküliku teine külg (M): "))

    diagonaal=round(sqrt(N**2 + M**2), 1) # sqrt() math moodulist
    print(f"Ristküliku diagonaal on {diagonaal}. ")
except ValueError:
    print("Palun sisesta kehtiv number. ")


#Ülesanne 6
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = teepikkus / aeg

    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except ValueError:
    print("Viga: Palun sisesta andmed numbrina.")


#Ülesanne 7
try:
    # 1. Küsime kasutajalt 5 täisarvu
    arv1 = int(input("Sisesta 1. täisarv: "))
    arv2 = int(input("Sisesta 2. täisarv: "))
    arv3 = int(input("Sisesta 3. täisarv: "))
    arv4 = int(input("Sisesta 4. täisarv: "))
    arv5 = int(input("Sisesta 5. täisarv: "))

    # 2. Arvutame summa ja aritmeetilise keskmise
    summa = arv1 + arv2 + arv3 + arv4 + arv5
    keskmine = summa / 5

    print(f"\nArvude aritmeetiline keskmine on: {keskmine}")

    # 3. Küsime jagaja, et leida täisarvuline osa ja jääk
    jagaja = int(input("Sisesta arv, millega summa jagada: "))

    taisarvuline_osa = summa // jagaja
    jaak = summa % jagaja

    print(f"Summa ({summa}) jagatuna arvuga {jagaja}:")
    print(f"Täisarvuline osa: {taisarvuline_osa}")
    print(f"Jääk: {jaak}")

except ValueError:
    print("Viga: Palun sisesta ainult täisarve!")