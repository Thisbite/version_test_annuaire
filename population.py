import sqlite3
import streamlit as st


# Fonction pour se connecter à la base de données
def get_db_connection():
    conn = sqlite3.connect('data_entry.db')
    return conn


# Fonction principale pour le formulaire de saisie de données
def population():
    conn = get_db_connection()
    c = conn.cursor()
#La liste des indicateurs
    indicateur = st.selectbox("Sélectionner Indicateur",
                              ["Effectif de la population",
                               "Rapport de Masculinité (RM) en %",
                               "Nombre de Centres d'Etat Civil Principaux",
                               "Nombre de Centres d'Etat Civil Secondaires",
                               "Nombre de Naissances enregistrées à l'Etat Civil",
                               "Nombre de Naissances enregistrées dans les structures sanitaires",
                               "Nombre de Naissances enregistées dans les délais à l'Etat Civil",
                               "Nombre de Naissances enregistées  hors délais à l'Etat Civil",
                               "Nombre de Naissances enregistées  hors délais à l'Etat Civil",
                               "Nombre de Décès enregistés à l'Etat Civil",
                               "Nombre de Décès  enregistés dans les structures sanitaires",
                               "Nombre de mariages enregistrés à l'Etat Civil",
                               "Nombre de demandes de divorces introduites par le Tribunal de Première Instance (TPI) ",
                               "Nombre de Conciliations obtenues",
                               "Nombre de Divorces accordés par consentement mutuel",
                               "Nombre de Divorces accordés pour faute prononcées",
                               "Nombre de demande de  Divorces rejetés",
                               "Nombre de Divorces accordés par le Tribunal de Première Instance (TPI)  ",
                               "Nombre de Mariages accordés par le Tribunal de Première Instance (TPI)  ",
                               "Nombre de Naissances dans les centres d'Etat Civil Communal",
                               "Nombre de Naissances dans les centres d'Etat Civil Sous-préfectoral",
                               "Nombre de Décès dans les centres d'Etat Civil Communal",
                               "Nombre de Décès dans les centres d'Etat Civil Sous-préfectoral",
                               "Nombre de Mariages dans les centres d'Etat Civil Communal"
                               ])

    # Créer le formulaire
    with st.form("formulaire_saisie_donnees"):


        if indicateur == "Effectif de la population":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")
            departement = st.text_input("Département", value="-")
            valeur_departement = st.number_input("Valeur Départementale", min_value=0.0, value=0.0, format="%f")
            sexe = st.selectbox("Sexe", ["-", "M", "F"], index=0)
            valeur_sexe = st.number_input("Valeur par Sexe", min_value=0.0, value=0.0, format="%f")


        elif indicateur == "Rapport de Masculinité (RM) en %":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")
            sexe = st.selectbox("Sexe", ["-", "M", "F"], index=0)
            valeur_sexe = st.number_input("Valeur par Sexe", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Centres d'Etat Civil Principaux":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Centres d'Etat Civil Secondaires":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Naissances enregistrées à l'Etat Civil":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Naissances enregistrées dans les structures sanitaires":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Naissances enregistées dans les délais à l'Etat Civil":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Naissances enregistées hors délais à l'Etat Civil":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Décès enregistés à l'Etat Civil":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Décès enregistés dans les structures sanitaires":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de mariages enregistrés à l'Etat Civil":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de demandes de divorces introduites par le Tribunal de Première Instance (TPI)":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Conciliations obtenues":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Divorces accordés par consentement mutuel":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Divorces accordés pour faute prononcées":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de demande de Divorces rejetés":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Divorces accordés par le Tribunal de Première Instance (TPI)":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Mariages accordés par le Tribunal de Première Instance (TPI)":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Naissances dans les centres d'Etat Civil Communal":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Naissances dans les centres d'Etat Civil Sous-préfectoral":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Décès dans les centres d'Etat Civil Communal":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Décès dans les centres d'Etat Civil Sous-préfectoral":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        elif indicateur == "Nombre de Mariages dans les centres d'Etat Civil Communal":
            region = st.selectbox("Sélectionner Région", ["-", "Poro", "Autre région"], index=0)
            valeur_regionale = st.number_input("Valeur Régionale", min_value=0.0, value=0.0, format="%f")

        # Bouton de soumission
        soumis = st.form_submit_button("Soumettre")

        if soumis:
            # Soummission indicateur : Effectif de la population
            if indicateur == "Effectif de la population":
                c.execute('''
                    INSERT INTO form_data (indicator, region, valeur_regionale, department, valeur_departement, sexe, valeur_sexe)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (indicateur, region, valeur_regionale, departement, valeur_departement, sexe, valeur_sexe))

            conn.commit()
            st.success("Données soumises avec succès")

    conn.close()


# Appel de la fonction principale pour exécuter l'application
if __name__ == "__main__":
    population()
