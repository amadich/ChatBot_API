print("This Configuration For Rest your Taille of your File [Count] to 0")
input("Tyoe Enter To Continue ...")
from pickle import*
fc = open("../db/count.dat","wb")
d = {}
d["taille"] = 0
dump(d,fc)
fc.close()
print("Your Configuration Is Succusfle!")
input("Type Enter to exit ...")