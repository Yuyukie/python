import json

# 1. Lesture du fichier user.json
with open("/data/user.json", "r") as f:
    user_data = f.read()
    user_json_dict = json.loads(user_data)


# 2. afficher l'age

print(f"Age : {user_json_dict["age"]}")

# 3. afficher le second hobby

print(f"Second hobby : {user_json_dict["hobbies"][1]}")

# 4. afficher l'email 

print(f"Email : {user_json_dict["email"]}")
