while True:
    print("Vali ülesanne: ")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")
    valik=input("Sisesta ülesande number (1-6) või 'q' väljumiseks: ")
    if valik == '1':
        pass
    elif valik == '2':
        pass
    elif valik == '3':
        pass
    elif valik == '4':
        pass
    elif valik == '5':
        pass
    elif valik == '6':
        pass 
    elif valik.lower() == 'q':
        break
    else:
        print("Viga: Palun sisetsa number 1 - 6 või 'q' väljumiseks.")



if valik == '1':
    #Ül 1
    i = 0 #loendur
    kogus = 0
    while i < 15:
        arv = float(input(f"{i + 1}. arv: "))
        if arv.is_integer():
            kogus += 1
        i += 1
    print("Täisarve:", kogus)


elif valik == '2':
    #Ül 2
    try:
        A=int(input("Sisesta arv A: "))
        if A > 0:
            summa = 0
            for i in range(1, A + 1):
                summa += i
            print("Summa:", summa)
        else:
            print("Palun sisesta positiivne täisarv.")
    except ValueError:
        print("Palun sisesta kehtiv täisarv.")


elif valik == '3':
    #Ül 3 
    try:
        i=0
        korrutis = 1
        for i in range(8):
            arv = float(input(f"{i + 1}. arv: "))
            if arv > 0:
                korrutis *= arv
        print("Positiivsete arvude korrutis:", korrutis)
    except ValueError:
        print("Palun sisesta ainult numbrit.")


elif valik == '4':
    #Ül 4
    for i in range(10, 21):
        print(f"{i} ruut on {i ** 2}")


elif valik == '5':
    #Ül 5
    try:
        N = int(input("Mitu arvu sisestad (N)? "))
        summa = 0
        for i in range(N):
            arv = float(input(f"{i + 1}. arv: "))
            if arv < 0:
                summa += arv
        print("Negatiivsete arvude summa:", summa)
    except ValueError:
        print("Palun sisesta kehtiv arv!")


elif valik == '6':
    #Ül 6
    try:
        N = int(input("Mitu arvu sisestad (N)? "))
        neg = 0
        pos = 0
        nullid = 0
        for i in range(N):
            arv = float(input(f"{i + 1}. arv: "))
            if arv < 0:
                neg += 1
            elif arv > 0:
                pos += 1
            else:
                nullid += 1
        print("Negatiivseid:", neg)
        print("Positiivseid:", pos)
        print("Nulle:", nullid)
    except ValueError:
        print("Palun sisesta kehtiv arv!")

elif valik.lower() == 'q':
    print("Programmist väljumine...")


