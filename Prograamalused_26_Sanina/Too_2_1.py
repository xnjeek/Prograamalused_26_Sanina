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
   
