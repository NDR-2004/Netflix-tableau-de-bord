import streamlit as st
from se_connecter import check_data_connection
from create_account import collect_and_store_user_data

# Page principale
st.title("Page de connexion")

# Onglets pour la connexion et la création de compte
tab1, tab2 = st.tabs(["Se connecter", "Créer un compte"])

# -----------------------------
# Onglet : Connexion
# -----------------------------
with tab1:
    st.header("Connexion")
    email = st.text_input("Email", placeholder="Entrez votre email")
    password = st.text_input("Mot de passe", placeholder="Entrez votre mot de passe", type="password")

    if st.button("Se connecter"):
        if email and password:
            try:
                check_data_connection([email, password])
                st.success("Connexion réussie !")
            except Exception as e:
                st.error(f"Erreur lors de la connexion : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")

# -----------------------------
# Onglet : Création de compte
# -----------------------------
with tab2:
    st.header("Créer un compte")

    name = st.text_input("Nom", placeholder="Entrez votre nom")
    first_name = st.text_input("Prénom", placeholder="Entrez votre prénom")
    age = st.text_input("Âge", placeholder="Entrez votre âge")
    telephone = st.text_input("Téléphone", placeholder="Entrez votre numéro de téléphone")
    email = st.text_input("Email", placeholder="Entrez votre email")
    adresse = st.text_input("Adresse", placeholder="Entrez votre adresse")
    password = st.text_input("Mot de passe", placeholder="Entrez un mot de passe", type="password")

    if st.button("Créer un compte"):
        if all([name, first_name, age, telephone, email, adresse, password]):
            try:
                collect_and_store_user_data([(name, first_name, age, telephone, email, adresse, password)])
                st.success("Compte créé avec succès !")
            except Exception as e:
                st.error(f"Erreur lors de la création du compte : {e}")
        else:
            st.warning("Veuillez remplir tous les champs.")
