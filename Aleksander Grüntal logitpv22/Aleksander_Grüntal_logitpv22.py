from math import * #*-kõik funktdioonid on vaja kasutada. kasutame: math.sin()
#import math kasutame: math.sin()
#2.osa Math kasutamine
print("Ristküliku ja ringi pindalad")
a=float(input("Anna laius: "))
b=float(input("Anna kõrgus: "))
S=a*b #+,-,/,*,**,sqrt(),// 5//2=2,% 5%2=1
d=sqrt(a**2+b**2)
r=float(input("Anna raadius: "))
Skr=pi*r**2
print(f"Ristküliku pindala on {S}. Ringi pindala on {round(Skr,2)}.")




#1. osa print(), impot(), int(), float()
print("Tere tulemast!") #print() teksti või andmete väljastuseks
nimi=input("Mis on sinu nimi? ") #Sisendi lugemine akraanil "..." ja ootab , kuni kasutaja vajutab Enter klahvi 
# input() -> str
print(f"{nimi}, sul on väga ilus nimi!")
print(nimi,", sul on väga ilus nimi!") #kui on erinevat andmete tüübid
print(nimi+", sul on väga ilus nimi!") #kui on sarnane andmete tüüp
vanus=int(input("kui vana sa oled?")) #input -> int
print(f"{nimi} Jargmisel aastal saad {vanus+1}") #muutuja vanus ei muuda
print("Aga selle aastal on ", vanus)
vanus+=1 #muudame muutuja väärtus
print (f"Järgmine aasta on käes, siis {nimi} on {vanus} aastat vana")
pikkus=float(input("mis on sinu pikkus?")) #imput() -> float: 1.75
print(f"{nimi} on {vanus} aastat vana ja suurepärase pikkusega {pikkus}")
