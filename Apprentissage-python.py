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