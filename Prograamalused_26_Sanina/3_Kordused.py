#while-tsükkel
x = 0
while x < 30:
    if x % 2 == 1:
        print(x, end=" ")
    x += 1


#while True ja break
x = 0
while True:
    if x % 2 == 1:
        print(x, end=" ")
    if x == 30:
        break
    x += 1


#for-tsükkel
for i in range(1, 31, 2):
    print(i, end=" ")


#Summa ja keskmine
kogus = int(input("N: "))
summa = 0
i = 1
while i <= kogus:
    summa = summa + i
    i = i + 1
print("Summa:", summa)
print("Keskmine:", summa / kogus)


#Loendamine ja suurim
kogus = 0
suurim = None
for i in range(5):
    arv = float(input(f"{i + 1}. arv: "))
    if arv > 0:
        kogus += 1
    if suurim is None or arv > suurim:
        suurim = arv
print("Positiivseid arve:", kogus)
print("Suurim arv:", suurim)


#Pesastatud tsüklid
for rida in range(1, 4):
    for veerg in range(0, 10):
        print(veerg, end=" ")
    print()    # rea lõpp


