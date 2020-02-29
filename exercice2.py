
def str2bool(v):
  return v.lower() in ("yes", "y")

zero = str2bool(input("La temperature est elle inferieure a 0 y/n : "))

cent = str2bool(input("La temperature est elle superieur a 100 y/n : "))

#zero = False
#cent = Cent

if not zero and  not cent: # F and F
    print("Il s'agit de l'eau liquide")
    out= True
elif  not zero and cent: #F and T
    print("Il s'agit de la vapeur d'eau")
    out= True
elif zero and not cent:# T and F
    print("Il s'agit de la glace")
    out= True
else:#T and T
    print("Impossible")
