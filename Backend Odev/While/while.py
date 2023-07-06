import random
liste = ["Ahmet","Enes","Burak","Derya","Beyza"]
listeKazanan = []
i = 5
while i>0:
    a = random.choice(liste)
    if a in listeKazanan:
        continue
    else:
        print("Kazanan: ",a)
        listeKazanan.append(a)
        i -=1