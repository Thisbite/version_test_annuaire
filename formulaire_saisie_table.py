import sqlite3



def insert_region(region_id, nom_region):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Region (region_id, nom_region) VALUES (?, ?)", (region_id, nom_region))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Exception in insert_region: {e}")
        return False


import streamlit as st

st.title("Enregistrement des Régions")

with st.form("region_form"):
    region_id = st.number_input("ID de la Région", min_value=1, step=1)
    nom_region = st.text_input("Nom de la Région")

    submitted = st.form_submit_button("Enregistrer")
    if submitted:
        success = insert_region(region_id, nom_region)
        if success:
            st.success("Région enregistrée avec succès")
        else:
            st.error("Erreur lors de l'enregistrement de la région")

def insert_departement(departement_id, f_region_id, nom_departement):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Departement (departement_id, f_region_id, nom_departement) VALUES (?, ?, ?)",
                           (departement_id, f_region_id, nom_departement))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Exception in insert_departement: {e}")
        return False


st.title("Enregistrement des Départements")

with st.form("departement_form"):
    departement_id = st.number_input("ID du Département", min_value=1, step=1)
    f_region_id = st.number_input("ID de la Région", min_value=1, step=1)
    nom_departement = st.text_input("Nom du Département")

    submitted = st.form_submit_button("Enregistrer")
    if submitted:
        success = insert_departement(departement_id, f_region_id, nom_departement)
        if success:
            st.success("Département enregistré avec succès")
        else:
            st.error("Erreur lors de l'enregistrement du département")

def insert_sous_prefecture(sousprefect_id, f_departement_id, nom_sousprefecture):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SousPrefectures (sousprefect_id, f_departement_id, nom_sousprefecture) VALUES (?, ?, ?)",
                           (sousprefect_id, f_departement_id, nom_sousprefecture))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Exception in insert_sous_prefecture: {e}")
        return False


st.title("Enregistrement des Sous-Préfectures")

with st.form("sous_prefecture_form"):
    sousprefect_id = st.number_input("ID de la Sous-Préfecture", min_value=1, step=1)
    f_departement_id = st.number_input("ID du Département", min_value=1, step=1)
    nom_sousprefecture = st.text_input("Nom de la Sous-Préfecture")

    submitted = st.form_submit_button("Enregistrer")
    if submitted:
        success = insert_sous_prefecture(sousprefect_id, f_departement_id, nom_sousprefecture)
        if success:
            st.success("Sous-Préfecture enregistrée avec succès")
        else:
            st.error("Erreur lors de l'enregistrement de la sous-préfecture")


def insert_domaine(domaine_id, nom_domaine):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Domaine (domaine_id, nom_domaine) VALUES (?, ?)", (domaine_id, nom_domaine))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Exception in insert_domaine: {e}")
        return False


st.title("Enregistrement des Domaines")

with st.form("domaine_form"):
    domaine_id = st.number_input("ID du Domaine", min_value=1, step=1)
    nom_domaine = st.text_input("Nom du Domaine")

    submitted = st.form_submit_button("Enregistrer")
    if submitted:
        success = insert_domaine(domaine_id, nom_domaine)
        if success:
            st.success("Domaine enregistré avec succès")
        else:
            st.error("Erreur lors de l'enregistrement du domaine")



def insert_sous_domaine(sous_domaine_id, f_domaine_id, nom_sous_domaine):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SousDomaine (sous_domaine_id, f_domaine_id, nom_sous_domaine) VALUES (?, ?, ?)",
                           (sous_domaine_id, f_domaine_id, nom_sous_domaine))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Exception in insert_sous_domaine: {e}")
        return False


st.title("Enregistrement des Sous-Domaines")

with st.form("sous_domaine_form"):
    sous_domaine_id = st.number_input("ID du Sous-Domaine", min_value=1, step=1)
    f_domaine_id = st.number_input("ID du Domaine", min_value=1, step=1)
    nom_sous_domaine = st.text_input("Nom du Sous-Domaine")

    submitted = st.form_submit_button("Enregistrer")
    if submitted:
        success = insert_sous_domaine(sous_domaine_id, f_domaine_id, nom_sous_domaine)
        if success:
            st.success("Sous-Domaine enregistré avec succès")
        else:
            st.error("Erreur lors de l'enregistrement du sous-domaine")


def insert_indicateur(indicateur_id, f_sous_domaine_id, nom_indicateur):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Indicateur (indicateur_id, f_sous_domaine_id, nom_indicateur) VALUES (?, ?, ?)",
                           (indicateur_id, f_sous_domaine_id, nom_indicateur))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Exception in insert_indicateur: {e}")
        return False


st.title("Enregistrement des Indicateurs")

with st.form("indicateur_form"):
    indicateur_id = st.number_input("ID de l'Indicateur", min_value=1, step=1)
    f_sous_domaine_id = st.number_input("ID du Sous-Domaine", min_value=1, step=1)
    nom_indicateur = st.text_input("Nom de l'Indicateur")

    submitted = st.form_submit_button("Enregistrer")
    if submitted:
        success = insert_indicateur(indicateur_id, f_sous_domaine_id, nom_indicateur)
        if success:
            st.success("Indicateur enregistré avec succès")
        else:
            st.error("Erreur lors de l'enregistrement de l'indicateur")


def insert_sexe(sexe_id, sexe):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Sexe (sexe_id, sexe) VALUES (?, ?)", (sexe_id, sexe))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Exception in insert_sexe: {e}")
        return False


def insert_groupe_age(grp_age_id, groupe_age):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO GroupeAge (grp_age_id, groupe_age) VALUES (?, ?)"
            cursor.execute(query, (grp_age_id, groupe_age))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_groupe_age: {e}")

def insert_age(age_id, age):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO Age (age_id, age) VALUES (?, ?)"
            cursor.execute(query, (age_id, age))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_age: {e}")

def insert_direction_statistique(direction_id, description):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO DirectionStatistique (direction_id, description) VALUES (?, ?)"
            cursor.execute(query, (direction_id, description))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_direction_statistique: {e}")

def insert_directeur(id, nom, prenom, email, numero):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO Directeur (id, nom, prenom, email, numero) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (id, nom, prenom, email, numero))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_directeur: {e}")

def insert_agent_collecte(id, nom, prenom, email, numero):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO AgentCollecte (id, nom, prenom, email, numero) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (id, nom, prenom, email, numero))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_agent_collecte: {e}")