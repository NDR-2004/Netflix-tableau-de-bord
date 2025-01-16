from Mysql_connexion_BDD import MySQL_connexion
import bcrypt

def collect_and_store_user_data(liste):
    #print("Vous allez créer votre compte, veuillez remplir les champs !")
    name = liste[0][0]
    first_name = liste[0][1]
    age = liste[0][2]
    telephone = liste[0][3]
    email = liste[0][4]
    adresse = liste[0][5]
    password = liste[0][6]

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    connection = MySQL_connexion()
    if connection is None:
        print("Nous sommes désolés, impossible de se connecter à la base de données.")
        return
    try:
        cursor = connection.cursor()

        insert_user_query = """
            INSERT INTO users (name, first_name, age, telephone, email, adresse, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        user_data = (name, first_name, age, telephone, email, adresse, hashed_password)

        cursor.execute(insert_user_query, user_data)
        connection.commit()
        print(f"Welcome {name}, votre compte a bien été créé.")

        # Demander si l'utilisateur veut revenir à l'écran d'accueil
        """se_connecter = input("Voulez-vous revenir à l'écran d'accueil ? oui/non : ")
        if se_connecter.lower() == "oui":
            print("Vous allez être redirigé vers l'écran d'accueil. Merci d'avoir créé un compte.")
            main_menu()  # Appel à la fonction d'accueil
        else:
            print("Au revoir.")"""
    except Exception as e:
        print(f"Erreur lors de l'insertion des données : {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("...")

