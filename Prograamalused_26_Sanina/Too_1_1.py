from random import * #randint


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
vanus=18 #int-täisarv
eesnimi="Anna" #str-sõne
pikkus=17.5 #float-kümnenmurd/ujukomaarv
kes_käib_koolis=True #bool-tõeväärtus
print(f"Vanus:{vanus}, tüüp:{type(vanus)}")
print(f"Eesnimi:{eesnimi}, tüüp:{type(eesnimi)}")
print(f"Pikkus:{pikkus}, tüüp:{type(pikkus)}")
print(f"Käib koolis:{kas_käib_koolis}, tüüp:{type(kas_käib_koolis)}")


#Ülesanne 3
kommide_arv=randit(1, 100)       #int(input("Kommide arv: "))
print(f"Laud on {kommide_arv} kommi.")
kommid=int(input("Mitu kommi soovid ära võtta? "))
kommide_arv -= kommid
print(f"Laud on nüüd {kommide_arv} kommi. ")
