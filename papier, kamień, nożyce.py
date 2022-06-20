import random

z=0
e=0

def essa(z,e):
    if z==10:
        print("KOMPUTER KOKS")
        return "dis"
    if e==10:
        print("GRACZ KOKS")
        return "dis"
    slowo = random.choice(["papier", "kamien", "nozyce"])
    gracz = input("papier, kamien czy nozyce? ")
    if z != 10 and e != 10:
        if slowo=="papier" and gracz =="kamien" or slowo=="kamien" and gracz =="nozyce" or slowo=="nozyce" and gracz =="papier":
            z=z+1
            print(f"{slowo}: {gracz} \t Komputer zdobywa punkt \t Komputer {z} : Gracz {e}")
            essa(z,e)
        elif slowo==gracz:
            print(f"{slowo}: {gracz} \t Remis                  \t Komputer {z} : Gracz {e}")
            essa(z,e)
        else:
            e=e+1
            print(f"{slowo}: {gracz} \t Gracz zdobywa punkt    \t Komputer {z} : Gracz {e}")
            essa(z,e)


essa(z,e)