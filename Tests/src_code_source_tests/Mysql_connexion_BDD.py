import mysql.connector
from mysql.connector import Error

# Configuration de la base de données
def MySQL_config():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Nahem2004',
        'database': 'Portfolio_Boursier'
    }
    return config

# Connexion unique à la base de données
def MySQL_connexion():
    try:
        connection = mysql.connector.connect(**MySQL_config())
        if connection.is_connected():
            print("Connexion réussie à la base de données MySQL")
            db_info = connection.get_server_info()
            print(f"Version MySQL du serveur : {db_info}")
        return connection
    except Error as e:
        print(f"Erreur lors de la connexion : {e}")
        return None

