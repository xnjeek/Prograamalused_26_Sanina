from ast import Try, TryStar
from datetime import date

#Ülesanne 1
# 1. Tervitus ja tänane kuupäev (Приветствие и дата)
tana = date.today()
print("Tere! Täna on", tana)

# 2. Erinevad formaadid (Различные форматы вывода)
print(tana.strftime("%d/%m/%Y"))  # Päev/Kuu/Aasta numbritega
print(tana.strftime("%B %d, %Y"))  # Kuu nimi tekstina
print(tana.strftime("%m/%d/%y"))  # Ameerika formaat
print(tana.strftime("%b-%d-%y"))  # Lühendatud kuu nimi

# 3. Päevad kuu ja aasta lõpuni (Дни до конца месяца и года)
# Lihtne näide: oletame, et kuus on 31 päeva ja aastas 365 päeva
paeva_kuu_lopuni = 31 - tana.day
paeva_aasta_lopuni = 365 - int(tana.strftime("%j")) 

print("Kuu lõpuni on jäänud umbes:", paeva_kuu_lopuni, "päeva")
print("Aasta lõpuni on jäänud umbes:", paeva_aasta_lopuni, "päeva")

# 4. Vanuse arvutamine (Расчет возраста - введите свой год, kuu и päev)
sünniaasta = 2005
vanus = tana.year - sünniaasta
print("Sinu vanus on umbes:", vanus, "aastat")


#Ülesanne 2
# Tehe sulgudega (Выражение со скобками)
vastus1 = 3 + 8 / (4 - 2) * 4
print("Vastus sulgudega on:", vastus1)

# Tehe ilma sulgudeta (Выражение без скобок)
vastus2 = 3 + 8 / 4 - 2 * 4
print("Vastus ilma sulgudeta on:", vastus2)

print("Selgitus: Sulud muudavad järjekorda. Esimesena arvutatakse (4 - 2).")


#Ülesanne 3
import math

# Küsime kasutajalt raadiuse (Запрашиваем радиус)
R = float(input("Sisesta ringi raadius (R): "))

külg = 2 * R

ruudu_pindala = külg * külg
ruudu_ümbermõõt = 4 * külg

ringi_pindala = math.pi * R * R
ringi_ümbermõõt = 2 * math.pi * R

print("Ruudu pindala:", round(ruudu_pindala, 2))
print("Ruudu ümbermõõt:", round(ruudu_ümbermõõt, 2))
print("Ringi pindala:", round(ringi_pindala, 2))
print("Ringi ümbermõõt:", round(ringi_ümbermõõt, 2))


#Ülesanne 4
import math

raadius_km = 6378
# Teisendame kilomeetrid meetriteks (Переводим км в метры)
raadius_m = raadius_km * 1000 

maa_ümbermõõt = 2 * math.pi * raadius_m
mündi_diameeter = 0.02575 # 2-eurone münt meetrites (25.75 mm)

müntide_arv = maa_ümbermõõt / mündi_diameeter

print("Maa ümbermõõt meetrites:", round(maa_ümbermõõt, 2))
print("Vaja läheb umbes:", round(müntide_arv), "münti")


#Ülesanne 5
rida1 = "kill-koll kill-koll killadi-koll "
rida2 = "kill-koll kill-koll kill-koll killadi-koll "
rida3 = "kill-koll kill-koll kill-koll kill-koll "
lõpp = "kill-koll"

kogu_tekst = rida1 + rida2 + rida3 + lõpp

# .title() teeb iga sõna alguse suureks täheks (Делает каждую первую букву заглавной)
print(kogu_tekst.title())


#Ülesanne 6
laul = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll koll.
"""

# Teeme kõik tähed suureks (Делаем все буквы большими)
print(laul.upper())


#Ülesanne 7
try:
    a = float(input("Sisesta ristküliku esimese külje pikkus: "))
    b = float(input("Sisesta ristküliku teise külje pikkus: "))

    pindala = a * b
    ümbermõõt = 2 * (a + b)

    print("Ristküliku pindala on:", pindala)
    print("Ristküliku ümbermõõt on:", ümbermõõt)
except ValueError:
    print("Viga: Palun sisesta ainult arvud!")

#Ülesanne 8
try:
    liitrid = float(input("Sisesta tangitud kütuse liitrid: "))
    kilomeetrid = float(input("Sisesta läbitud kilomeetrid: "))

    # Valem: (liitrid / kilomeetrid) * 100
    kulu = (liitrid / kilomeetrid) * 100

    print("Keskmine kütusekulu 100 km kohta on:", round(kulu, 2), "liitrit")
except ValueError:
    print("Liitrid ja kilomeetrid on arvud")


#Ülesanne 9 
kiirus = 29.9
try:
    M = float(input("Sisesta sõiduaeg minutites (M): "))

    # Jagame 60-ga, et saada tunnid (Делим на 60, чтобы получить часы)
    aeg_tundides = M / 60
    vahemaa = kiirus * aeg_tundides

    print("Rulluisutaja jõuab", M, "minutiga", round(vahemaa, 2), "km kaugusele.")
except ValueError:
    print("Viga: Palun sisesta ainult arvud!")


#Ülesanne 10
try:
    kogu_minutid = int(input("Sisesta aeg minutites: "))

    tunnid = kogu_minutid // 60  # Täistunnid (Целые часы)
    minutid = kogu_minutid % 60  # Ülejäänud minutid (Остаток минут)

    print("Vastus on:", tunnid, ":", minutid)
except ValueError:
    print("Viga: Palun sisesta ainult täisarvud!")
