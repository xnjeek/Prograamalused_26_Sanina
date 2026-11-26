#Ülesanne 10
for i in range(10):
    while True:
        try:
            a = float(input(f"{i + 1}. paar - esimene arv: "))
            b = float(input(f"{i + 1}. paar - teine arv: "))
            break
        except ValueError:
            print("Palun sisesta kehtiv arv.")
    if a > b:
        print(f"Suurem: {a}")
    elif b > a:
        print(f"Suurem: {b}")
    else:
        print("Võrdsed.")


print( )
#Ülesanne 12
while True:
    try:
        N = int(input("Niidukite arv N: "))
        m = float(input("Esimese niiduki tööaeg tundides m: "))
        if N > 0 and m >= 0:
            break
    except ValueError:
        print("Palun sisesta kehtiv arv.")

kokku = 0
praegune = m
for i in range(N):
    kokku += praegune
    praegune += 10 / 60

print(f"Kogu brigaad töötas kokku {kokku} tundi.")


print( )
#Ülesanne 13
kogus = 0
summa = 0

for i in range(100, 1001):
    if i % 7 == 0:
        print(i)
        kogus += 1
        summa += i

print(f"Arvude kogus: {kogus}")
print(f"Arvude summa: {summa}")


print( )
#Ülesanne 17
while True:
    try:
        arv = int(input("Sisesta täisarv korrutustabeli jaoks: "))
        break
    except ValueError:
        print("Palun sisesta kehtiv täisarv.")

for i in range(1, 10):
    print(f"{arv}*{i}={arv * i}")


print( )
#Ülesanne 31
while True:
    try:
        K = int(input("Mitu kotletti on (K)? "))
        M = int(input("Mitu kotletti mahub pannile (M > 0)? "))
        if K >= 0 and M > 0:
            break
        else:
            print("Kontrolli, et K >= 0 ja M > 0.")
    except ValueError:
        print("Palun sisesta kehtiv täisarv.")

tais_pannid = K // M
viimane_pann = K % M

print(f"Täis pannitäisi: {tais_pannid}")
print(f"Viimasele pannile jääb: {viimane_pann} kotletti")
