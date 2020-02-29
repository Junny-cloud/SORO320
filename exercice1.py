out = False
while out == False:
    temperature = input("Veillez rentre une temperature (dégres Celcius): ")
    try:
        temperature = int(temperature)
        if 0<temperature<100:
            print("Il s'agit de l'eau liquide")
            out= True
        elif temperature >= 100:
            print("Il s'agit de la vapeur d'eau")
            out= True
        elif temperature <= 0:
            print("Il s'agut de la glace")
            out= True
    
    except:
        print("!!!! Veillez ne pas entrer de chaines de caracteres !!!!!!")
