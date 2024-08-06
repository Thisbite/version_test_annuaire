import streamlit as st
import  sqlite3

#Connexion à la base de donnée
def get_db_connection():
    conn = sqlite3.connect('data_entry.db')
    return conn

def sante():
    conn = get_db_connection()
    c = conn.cursor()

    indicateur = st.selectbox("Sélectionner Indicateur",
                              ["Nombre d'infrastructures sanitaire",
                               "Nombre de personnel médical et paramédical"
                               ])

    # Créer le formulaire
    with st.form("formulaire_saisie_donnees"):
        if indicateur == "Nombre d'infrastructures sanitaire":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")
            departement = st.text_input("Département", value="-")
            valeur_departement = st.number_input("Valeur Départementale", min_value=0.0, value=0.0, format="%f")
            sexe = st.selectbox("Sexe", ["-", "M", "F"], index=0)
            valeur_sexe = st.number_input("Valeur par Sexe", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de personnel médical et paramédical":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")
            departement = st.text_input("Département", value="-")
            valeur_departement = st.number_input("Valeur Départementale", min_value=0.0, value=0.0, format="%f")
            sexe = st.selectbox("Sexe", ["-", "M", "F"], index=0)
            valeur_sexe = st.number_input("Valeur par Sexe", min_value=0.0, value=0.0, format="%f")
            type_personne_medical = st.selectbox("Type de personne médical", ["Medecin", "Infirmier"], index=0)
            valeur_type_personne_medical = st.number_input("Valeur par Type de personne médical", min_value=0.0,
                                                           value=0.0, format="%f")

        # Bouton de soumission
        soumis = st.form_submit_button("Soumettre")

        if soumis:
            # Construire la requête SQL en fonction de l'indicateur sélectionné
            if indicateur == "Effectif de la population":
                c.execute('''
                        INSERT INTO form_data (indicator, region, valeur_regionale, department, valeur_departement, sexe, valeur_sexe)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (indicateur, region, valeur_regionale, departement, valeur_departement, sexe, valeur_sexe))
            elif indicateur == "Nombre de personnel médical et paramédical":
                c.execute('''
                        INSERT INTO form_data (indicator, region, valeur_regionale, department, valeur_departement, sexe, valeur_sexe, type_personne_medical, valeur_type_personne_medical)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (indicateur, region, valeur_regionale, departement, valeur_departement, sexe, valeur_sexe,
                          type_personne_medical, valeur_type_personne_medical))

            conn.commit()
            st.success("Données soumises avec succès")

    conn.close()
    return