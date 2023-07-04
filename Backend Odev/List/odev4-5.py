# ODEV4
names = ["mehmet","derya","mustafa","buse"]
answer = input("Lutfen isim giriniz: ")
if answer in names:
    print("Hosgeldin {}".format(answer))
else:
    print(names)
# ODEV5
answer1 = input("Yeni isim")
names.insert(0,answer1)
print(names)