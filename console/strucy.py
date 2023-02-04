# here is admin you can remplire your file
# with message bot
from pickle import * 
def get_taille():
    fc = open("../db/count.dat","rb")
    x = load(fc)
    taille1 = x["taille"]
    print("You Tille in Last one is : ",taille1)
    n = int(input("Give me Taille => "))
    taille2 = taille1 + n
    # Add my taille in new File Count
    fc = open("../db/count.dat","wb")
    dk = {}
    dk["taille"] = taille2
    dump(dk,fc)
    while not n>0:
        n = int(input("Give me Taille => "))
    return n
def remplire(n):
    f = open("../db/api2.dat",'ab')
    t = [0]*n
    for i in range(n):
        d = {}
        d["req"] = input("Your Client Message : ")
        d["res"] = input("Your Server Message : ")
        t[i] = d
    dump(t,f)
    f.close()
    return t
def affiche(n,t):
    #f = open("db/api1.dat","rb")
    #x = load(f)
    for i in range(n):
        print("Your api => ",t[i])
    #f.close()
#programme General
n = get_taille()
t = remplire(n)
affiche(n,t)