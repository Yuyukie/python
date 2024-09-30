import random

secret = random.randint(0,100)
user_number = int(input('Veuillez entrer un nombre entre 0 et 100'))
attempts = 1

while secret != user_number :
    if secret < user_number :
        print("C\'est plus petit")
    else :
        print ("c\'est plus grand")
    
    user_number = int(input('Veuillez entrer un nombre entre 0 et 100'))
    attempts = attempts + 1

print(f"Bravo vous avez trouvé le nombre secret{secret}en {attempts}essai.s")