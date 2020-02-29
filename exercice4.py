age = int(input("saissivez l'age du conducteur "))
nbrPermis =int(input("saisissez la durée du permis en année du conducteur "))
nbrAccident = int(input("entrez le nombre d'accident commis par le conducteur "))

try:

    if age < 25  and nbrPermis < 2 and nbrAccident == 0 :
        tarif="rouge"
        print("tarif rouge  ")
    elif age < 25  and nbrPermis < 2 and nbrAccident != 0:
        tarif="refusé"
        print("refusé")
    elif (age < 25  and nbrPermis >2 ) or (age > 25  and nbrPermis < 2 ) and nbrAccident == 0:
        tarif="orange"
        print("tarif orange ")
    elif (age < 25  and nbrPermis >2 ) or (age > 25  and nbrPermis < 2 ) and nbrAccident == 1:
        tarif="rouge"
        print("tarif rouge  ")
    elif (age < 25  and nbrPermis >2 ) or (age > 25  and nbrPermis < 2 ) and nbrAccident > 1:
        tarif="refusé"
        print("refusé")
    elif age > 25  and nbrPermis > 2  and nbrAccident == 0:
        tarif="vert"
        print("tarif vert ")
    elif age > 25  and nbrPermis > 2  and nbrAccident == 1:
        tarif="orange"
        print("tarif orange ")
    elif age > 25  and nbrPermis > 2  and nbrAccident == 2:
        tarif="rouge"
        print(" tarif rouge ")
    elif age > 25  and nbrPermis > 2  and nbrAccident > 2 :
        tarif="refusé"
        print("refusé")

    if tarif != "refusé" and nbrPermis >= 5:
        if tarif == "rouge":
            print("pour vous encourager vous passez du tarif rouge a orange ")
        if tarif == "vert":
            print("pour vous encourager vous passez du tarif vert a bleu ")
        if tarif == "orange":
            print(" pour vous encourager vous passez du tarif orange a vert ")
  

except :
    print("il y'a pas d'offre valable")