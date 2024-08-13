import streamlit as st
import pandas as pd

# Créer un dataframe vide avec les colonnes souhaitées
df = pd.DataFrame(columns=["Nom", "Prénom", "Âge"])

# Titre de l'application
st.title("Formulaire pour remplir le tableau")

# Formulaire pour remplir le tableau
with st.form("formulaire_tableau"):
    # Créer trois colonnes
    col1, col2, col3 = st.columns(3)

    # Champs de formulaire dans les colonnes
    with col1:
        nom = st.text_input("Nom")
    with col2:
        prenom = st.text_input("Prénom")
    with col3:
        age = st.number_input("Âge", min_value=0, max_value=120, step=1)

    # Bouton de soumission
    submit = st.form_submit_button("Ajouter")

    # Si le bouton est cliqué, ajouter les données dans le dataframe
    if submit:
        new_data = pd.DataFrame({"Nom": [nom], "Prénom": [prenom], "Âge": [age]})
        df = pd.concat([df, new_data], ignore_index=True)

# Afficher le tableau
st.write("Tableau des données remplies :")
st.dataframe(df)
