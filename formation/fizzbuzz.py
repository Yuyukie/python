number = int(input("Veiillez saisir un nombre : "))

def fizzbuzz(A) :
    if number % 3 == 0 and number % 5 == 0 :
        print("c'est un multiple de 3 et de 5")
    elif number % 3 == 0 :
        print ("c'est un multiple de 3")
    elif number % 5 == 0 :
        print ("c'est un multiple de 5")
    else :
        print(number)


fizzbuzz(number)

def fizzbuzz2(B) :
    for i in range(1, B + 1) :
        if number % 3 == 0 and number % 5 == 0 :
            print("fizzbuzz")
        elif number % 3 == 0 :
            print ("fizz")
        elif number % 5 == 0 :
            print ("buzz")
        else :
            print(number)
        print(i)

fizzbuzz2(number)