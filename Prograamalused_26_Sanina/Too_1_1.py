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