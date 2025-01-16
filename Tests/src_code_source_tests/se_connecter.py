from Mysql_connexion_BDD import MySQL_connexion
import bcrypt

def check_data_connection(liste):
    identifiant_email = liste[0]
    password = liste[1]

    connection = MySQL_connexion()
    if connection is None:
        print("Problème de connexion à la base de données, veuillez nous en excuser.")
        return

    try:
        cursor = connection.cursor()

        recuperer_user_query = """
            SELECT name, email, password FROM users WHERE email = %s;
        """
        user_data = (identifiant_email,)
        cursor.execute(recuperer_user_query, user_data)

        resultat = cursor.fetchone()
        if resultat:
            name_recuperer = resultat[0]
            email_recuperer = resultat[1]
            password_hash = resultat[2]

            if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')) and email_recuperer == identifiant_email:
                print(f"Connexion réussie ! Bienvenue, {name_recuperer}.") # essaye de return
            else:
                print("Mot de passe ou email incorrect.") # essaye de return
        else:
            print("Utilisateur non trouvé.") # essaye de retourner
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("...")
