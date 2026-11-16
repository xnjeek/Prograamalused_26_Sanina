#Ülesanne 1
from ast import Try


eesnimi = input("Sisesta eesnimi: ")
if eesnimi.upper() == "JUKU":
   print("Lähme Jukuga kinno!")
if eesnimi.isupper():
        print("Ära karju, Juku!")
elif eesnimi.islower():
        print("Ära sosista, Juku!")
try:
    vanus = int(input("Kui vana sa oled, Juku? "))
    if 0 <=vanus < 6:
        pilet="tasutapilet"
    elif 6 <= vanus <= 14:
        print("lastepilet")
    elif 15 <= vanus <= 65:
        print("täispilet")
    elif 65<=vanus<100:
        pilet="sooduspilet"
    else:
        print("Viga andmetes. ")
    print(f"Juku vanus on {vanus} aastat, seega on vaja osta {pilet}.")
except ValueError:
    print("Palun sisesta oma vanus numbrina.")

else:
    print("Täna kinno ei minna. ")
   

#Ülesanne 2 
pinginaabrid=["Anna","Vika"]
nimi1=input("Sisesta esimese inimese nimi: ")
nimi2=input("Sisesta teise inimese nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
        print(f"{nimi1} ja {nimi2} on täna pinginaabbrid.")
    else:
        print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid.")
else:
    print("Viga: nimed peavad koosnema ainult tähtedest.")
#otsing nimede algustähtede järgi
valik=input("Kas soovid otsida nimede algustähtede järgi? (jah/ei): ").lower()
otsing=False
if valik=="jah":
    algustäht=input("Sisesta algustäht: ").capitalize()
    for nimi in pinginaabrid:
        if nimi.startswith(algustäht):
            print(f"{nimi} algab tähega {algustäht}.")
            otsing=True
    if not otsing:
        print(f"Ühtegi nime, mis algab tähega {algustäht}, ei leitud.")

else:
    print("Otsingut ei tehta.")


#Ülesanne 3 
try:
    pikkus=float(input("Sisesta toa pikkus meetrites: "))
    laius=float(input("Sisesta toa laius meetrites: "))
    pindala=pikkus*laius
    print(f"Põranda pindala on {round(pindala, 2)} ruutmeetrit.")
except ValueError:
    print("Viga: Palun sisesta numbrilised väärtused pikkuse ja laiuse jaoks.")

valik=input("Kas soovid remonti teha? (jah/ei): ").lower()
if valik=="jah":
    hind=float(input("Sisesta ruutmeetri hind: "))
    poranda_hind=pindala*hind
    print(f"Põranda vahetamise hind on {round(poranda_hind, 2)} eurot.")
    
#lisaküsimus
    tegija=input("Kas teed remondi ise või kasutad professionaali abi? (ise/professionaal): ").lower()
    if tegija=="professionaal":
        too_hind=float(input("Sisesta töö hind ruutmeetri kohta: "))
        koguhind=poranda_hind+(pindala*too_hind)
        print(f"Remondi koguhind koos tööga on {round(koguhind, 2)} eurot.")
    else:
        print(f"Remondi koguhind on {round(poranda_hind, 2)} eurot.")
else:
    print("Remonti ei tehta.")


#Ülesanne 4
toodete_arv = 4

print(f"Sisesta {toodete_arv} toote alghind:")

for i in range(1, toodete_arv + 1):
        try:
            alghind = float(input(f"{i}. toote alghind: "))
            
            if alghind < 0:
                print("Viga: Hind ei saa olla negatiivne!")
                
# Если цена больше 700, делаем скидку 30% (умножаем на 0.7)
            if alghind > 700:
                lopp_hind = round(alghind * 0.7, 2)
                print(f"Soodushind (30%): {lopp_hind:.2f} eurot")
            else:
                lopp_hind = round(alghind, 2)
                print(f"Lõpp hind: {lopp_hind:.2f} eurot (soodustust pole)")
            break
            
        except ValueError:
            print("Viga: Palun sisesta numbriline väärtus alhinna jaoks.")


#Ülesanne 5
try:
    temperatuur = float(input("Sisesta toatemperatuur: "))
    if temperatuur > 18:
        print("Temperatuur on üle 18 kraadi (soovitatav toasoojus talvel).")
    else:
        print("Temperatuur on 18 kraadi või madalam.")
except ValueError:
    print("Viga: Palun sisesta numbriline väärtus temperatuuri jaoks.")


#Ülesanne 6
try:
    pikkus = float(input("Sisesta oma pikkus sentimeetrites: "))
    if pikkus < 160:
        print("Oled lühike.")
    elif 160 <= pikkus <= 185:
        print("Oled keskmise pikkusega.")
    else:
        print("Oled pikk.")
except ValueError:
    print("Viga: Palun sisesta pikkus numbritena.")


#Ülesanne 7
try:
    sugu = input("Sisesta oma sugu (m / n / mees / naine): ").lower()
    
    if sugu == "m" or sugu == "mees":
        pikkus = float(input("Sisesta oma pikkus sentimeetrites: "))
        if pikkus < 170:
            print("Oled lühike mees.")
        elif 170 <= pikkus <= 190:
            print("Oled keskmise pikkusega mees.")
        else:
            print("Oled pikk mees.")
            
    elif sugu == "n" or sugu == "naine":
        pikkus = float(input("Sisesta oma pikkus sentimeetrites: "))
        if pikkus < 155:
            print("Oled lühike naine.")
        elif 155 <= pikkus <= 175:
            print("Oled keskmise pikkusega naine.")
        else:
            print("Oled pikk naine.")
            
    else:
        print("Viga: Sugu on sisestatud valesti!")
        
except ValueError:
    print("Viga: Palun sisesta pikkus numbrilise väärtusena.")


#Ülesanne 8
import random

h_piim = round(random.uniform(0.5, 3), 2)
h_sai = round(random.uniform(0.5, 3), 2)
h_leib = round(random.uniform(0.5, 3), 2)
h_juust = round(random.uniform(0.5, 3), 2)
h_vorst = round(random.uniform(0.5, 3), 2)

kokku = 0
tsekk = ""

if input(f"Kas soovid osta piima ({h_piim} €)? (jah/ei): ").lower() == "jah":
    k = input("Kogus: ")
    if k.isdigit():
        s = round(h_piim * int(k), 2)
        kokku += s
        tsekk += f"Piim: {k} tk x {h_piim} € = {s} €\n"

if input(f"Kas soovid osta saia ({h_sai} €)? (jah/ei): ").lower() == "jah":
    k = input("Kogus: ")
    if k.isdigit():
        s = round(h_sai * int(k), 2)
        kokku += s
        tsekk += f"Sai: {k} tk x {h_sai} € = {s} €\n"

if input(f"Kas soovid osta leiba ({h_leib} €)? (jah/ei): ").lower() == "jah":
    k = input("Kogus: ")
    if k.isdigit():
        s = round(h_leib * int(k), 2)
        kokku += s
        tsekk += f"Leib: {k} tk x {h_leib} € = {s} €\n"

if input(f"Kas soovid osta juustu ({h_juust} €)? (jah/ei): ").lower() == "jah":
    k = input("Kogus: ")
    if k.isdigit():
        s = round(h_juust * int(k), 2)
        kokku += s
        tsekk += f"Juust: {k} tk x {h_juust} € = {s} €\n"

if input(f"Kas soovid osta vorsti ({h_vorst} €)? (jah/ei): ").lower() == "jah":
    k = input("Kogus: ")
    if k.isdigit():
        s = round(h_vorst * int(k), 2)
        kokku += s
        tsekk += f"Vorst: {k} tk x {h_vorst} € = {s} €\n"

print("\n TŠEKK ")
print(tsekk)
print(f"Kogusumma: {round(kokku, 2)} €")

