import tkinter as tk
from se_connecter import check_data_connection
from create_account import collect_and_store_user_data

class Interface:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Page de connexion")
        self.fenetre.geometry("400x400")
        self.fenetre_creer_compte = None # initialisation différente pour éviter deux tK
        self.reglage_connection_fenetre()

    def reglage_connection_fenetre(self):
        # widget de la fenetre de connexion
        self.zone_texte_email = tk.Entry(self.fenetre, width=20, bg="white")
        self.zone_texte_email.pack(pady=5)
        self.zone_texte_mp = tk.Entry(self.fenetre, width=20, bg="white")
        self.zone_texte_mp.pack(pady=5)

        button_connecter = tk.Button(self.fenetre, text="Se connecter", bg="orange", fg="black", command=self.connection)
        button_connecter.pack(pady=10)
        button_creer_un_compte = tk.Button(self.fenetre, text="Creer un compte", bg="orange", fg="black", command=self.ouvrir_creer_compte_fenetre)
        button_creer_un_compte.pack(pady=10)

    def connection(self):
        # recupere les données des champs et appelle la fonction de connexion
        mail = self.zone_texte_email.get()
        mp = self.zone_texte_mp.get()

        if mail and mp:
            try:
                check_data_connection([mail, mp]) # appelle de la fonction (se_connecter.py)
                print("connexion réussie")
            except Exception as e:
                print(f"Erreur lor de la connexion : {e}")
        else:
            print("Veuillez remplir tous les champs")

    def ouvrir_creer_compte_fenetre(self):
        if self.fenetre_creer_compte is not None:
            return

        self.fenetre_creer_compte = tk.Toplevel(self.fenetre)
        self.fenetre_creer_compte.title("Créer un compte")
        self.fenetre_creer_compte.geometry("400x400")
        self.fenetre_creer_compte.protocol("WM_DELETE_WINDOW", self.fermer_creer_un_compte_fenetre)

        # widgets de la fenetre de creation de compte
        self.name = tk.Entry(self.fenetre_creer_compte, width=20, bg="white")
        self.name.pack(pady=5)

        self.first_name = tk.Entry(self.fenetre_creer_compte, width=20, bg="white")
        self.first_name.pack(pady=5)

        self.age = tk.Entry(self.fenetre_creer_compte, width=20, bg="white")
        self.age.pack(pady=5)

        self.telephone = tk.Entry(self.fenetre_creer_compte, width=20, bg="white")
        self.telephone.pack(pady=5)

        self.email = tk.Entry(self.fenetre_creer_compte, width=20, bg="white")
        self.email.pack(pady=5)

        self.adresse = tk.Entry(self.fenetre_creer_compte, width=20, bg="white")
        self.adresse.pack(pady=5)

        self.password = tk.Entry(self.fenetre_creer_compte, width=20, bg="white")
        self.password.pack(pady=5)

        button_creer = tk.Button(self.fenetre_creer_compte, text="Creer un compte", bg="orange", fg="black", command=self.creer_compte)
        button_creer.pack(pady=10)

    def creer_compte(self):
        # recuperer les données des champs et appelle la fonction de creation de compte
        name = self.name.get()
        first_name = self.first_name.get()
        age = self.age.get()
        telephone = self.telephone.get()
        email = self.email.get()
        adresse = self.adresse.get()
        password = self.password.get()

        if all([name, first_name, age, telephone, email, adresse, password]):
            try:
                collect_and_store_user_data([(name, first_name, age, telephone, email, adresse, password)])
                print("compte créer avec succcès")
                self.fermer_creer_un_compte_fenetre()
            except Exception as e:
                print(f"Erreur lors de la création du compte : {e}")
        else:
            print("Veuillez remplir tous les champs")

    def fermer_creer_un_compte_fenetre(self):
        self.fenetre_creer_compte.destroy()
        self.fenetre_creer_compte = None

# lancer l'interface
if __name__ == "__main__":
    app = Interface()
    app.fenetre.mainloop()
