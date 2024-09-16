celsius = float(input ("Entrz une température en celsius : ") )
fahrenheit = celsius * 9/5 +32
print (celsius, "degrés Celsius équivalent à", fahrenheit, "degrés fahrenheit")

moyenne = float(input("Quelle est votre moyenne"))

if 12 <= moyenne < 14:
    print("Assez bien")
elif 14 <= moyenne < 16:
    print("Bien")
elif 16 <= moyenne < 18:
    print("Tres bien")
elif moyenne >= 18:
    print("Félicitations")
else:
    print("Pas de mention")

nb_vies = 7
mot_mystere = "python"
mot_public = "_"*len(mot_mystere)

while nb_vies > 0 and mot_mystere != mot_public :
    lettre = str(input("Propose une lettre : "))
    if (lettre) in mot_mystere :
        for i in range(len(mot_mystere)) :
            if mot_mystere[i] == lettre :
                mot_public = mot_public[:i] + lettre + mot_public[i + 1:]
    else :
        nb_vies -= 1
    if mot_public == mot_mystere:
        print("Bravo ! Le mot est", mot_mystere)
    elif nb_vies ==0 :
        print("vous avez perdu")
    else :
        print("vous avez", nb_vies)
        print("le mot est :", mot_public)

