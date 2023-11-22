# 1.Feladat Írj programot, ami kiírja a képernyőre, hogy ”Hello world!”!
szovegKiir = f"Hello World!"
print(szovegKiir)

# ˝2.Feladat Írj programot, beolvassa a felhasználó nevét, majd köszön neki!

#Változók
nev, szovegKiir = "", ""

nev = input("Hogy hívnak: ")

szovegKiir = f"Hello {nev}!"

# ˝3.Feladat Írj programot, ami beolvas egy számot, majd kiírja a kétszeresét!

alapSzam, ketszeres, szovegKiir = 0, 0, ""

alapSzam = int(input("Kérem a számo: "))
ketszeres = 2 * alapSzam
szovegKiir = f"A szám: {alapSzam} \
kétszerese: {ketszeres}"

print(szovegKiir)

"""
Írj programot, ami beolvas két számot, majd kiírja:
a. az összegüket;
b. különbségüket;
c. szorzatukat;
d. hányadosukat, ha lehet!
"""

elso, masodik, osszeg, kulonbseg, szorzat, hanyados, szovegKiir = 0, 0, 0, 0, 0, 0.0, ""

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem az második számot: "))

osszeg = elso + masodik
kulonbseg = elso - masodik
szorzat = elso * masodik
hanyados = elso / masodik

szovegKiir = f"A számok: {elso}, {masodik}"
szovegKiir += f"\nösszeg: {osszeg}"
szovegKiir += f"\nKülönbsége: {kulonbseg}"
szovegKiir += f"\nszorzata: {szorzat}"
szovegKiir += f"\nhányadosa: {hanyados:.4f}"

print(szovegKiir)

# 5.Feladat Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

elso, masodik, nagyobb, szovegKiir = 0, 0, 0, ""

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem az második számot: "))

if elso <=masodik:
    nagyobb = masodik
else:
    nagyobb = elso

szovegKiir = f"A nagyobb szám: {nagyobb}"

print(szovegKiir)

# ¨6.Feladat . Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet! 

elso, masodik, harmadik, legkissebb, szovegKiir = 0, 0, 0, 0, ""

kissebb = 0

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))
harmadik = int(input("Kérem a harmadik számot: "))

if elso <= masodik:
    kisebb = elso
else:
    kisebb = masodik

if kisebb <= harmadik:
    legkisebb = kisebb
else:
    legkisebb = harmadik

szovegKiir = f"A legkissebb szám: {legkisebb}"
print(szovegKiir)