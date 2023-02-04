# show my file
from pickle import*

fc = open("../db/count.dat","rb")
x = load(fc)
n = x["taille"]
f = open("../db/api1.dat","rb")
for i in range(n):
    x = load(f)
    print(x)