import random

def otos_sorsolas():
    szamok = []
    for x in range(0, 5):
        szamok.append(random.randint(1, 90))
    return szamok

def hatos_sorsolas():
    szamok = []
    for x in range(0, 6):
        szamok.append(random.randint(1, 45))
    return szamok

def otos_kivalasztva():
    print("✅ Ötös lottó kiválasztva")
    szamok = otos_sorsolas()
    felhasznaloi_szamok = otos_input()
    print(f"\n\n🔢 A te számaid: \n{', '.join(map(str, felhasznaloi_szamok))}")
    print(f"🎰 A nyerő számok:\n{', '.join(map(str, szamok))}")
    if felhasznaloi_szamok == szamok:
        print("\n🏆 Nyertél! ")
    elif felhasznaloi_szamok != szamok:
        print("\n😭 Nem nyertél! ")   
    for i in range(5):
        matches = 0
        if szamok[i] == felhasznaloi_szamok[i]:
            matches += 1
    print(f"\n{matches} számod talált!")


def hatos_kivalasztva():
    print("✅ Hatos lottó kiválasztva")
    szamok = hatos_sorsolas()
    felhasznaloi_szamok = hatos_input()
    print(f"\n\n🔢 A te számaid: \n{', '.join(map(str, felhasznaloi_szamok))}")
    print(f"🎰 A nyerő számok:\n{', '.join(map(str, szamok))}")
    if felhasznaloi_szamok == szamok:
        print("\n🏆 Nyertél! ")
    elif felhasznaloi_szamok != szamok:
        print("\n😭 Nem nyertél! ")   
    for i in range(6):
        matches = 0
        if szamok[i] == felhasznaloi_szamok[i]:
            matches += 1
    print(f"\n{matches} számod talált!")

def main():
    print("Szerencsejáték Zrt. 🍀")
    print("Kérlek válaszd ki milyen típusú lottót szeretnél játszani!\n5-ös lottó\n6.-os lottó\nKiválasztani úgy tudod, hogy az adott lottó indexét beírod (1,2)")
    valasztott_lotto = input("Választás: ")
    if valasztott_lotto == "1":
        otos_kivalasztva()
    elif valasztott_lotto == "2":
        hatos_kivalasztva()
    else: 
        print("Választás nem érelmezhető, kérlek próbáld újra")
        main()

def hatos_input():
    felhasznaloi_szamok = []
    sorszam = 0
    while sorszam < 6:
        szam = int(input(f"Mi az {sorszam + 1}. számod? ")) 
        if szam in felhasznaloi_szamok < 0: 
            print("A megadott szám helytelen/érvénytelen! ")
        elif szam in felhasznaloi_szamok > 90:
            print("A megadott szám helytelen/érvénytelen! ")
        elif szam in felhasznaloi_szamok:
            prin("A megadott szám már szerepel a tippelt számok között! ")
        else:
            felhasznaloi_szamok.append(szam)
            felhasznaloi_szamok.sort()
            sorszam += 1

def otos_input():
    felhasznaloi_szamok = []
    sorszam = 0
    while sorszam < 5:
        szam = int(input(f"Mi az {sorszam + 1}. számod? ")) 
        if szam < 0: 
            print("A megadott szám helytelen/érvénytelen! ")
        elif szam > 90:
            print("A megadott szám helytelen/érvénytelen! ")
        elif szam in felhasznaloi_szamok:
            print("A megadott szám már szerepel a tippelt számok között! ")
        else:
            felhasznaloi_szamok.append(szam)
            felhasznaloi_szamok.sort()
            sorszam += 1
    return felhasznaloi_szamok

main()