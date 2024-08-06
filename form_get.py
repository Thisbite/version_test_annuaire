import sqlite3

def insert_domaine(domaine_id, nom_domaine):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO Domaine (domaine_id, nom_domaine) VALUES (?, ?)"
            cursor.execute(query, (domaine_id, nom_domaine))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_domaine: {e}")

def insert_sous_domaine(sous_domaine_id, f_domaine_id, nom_sous_domaine):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO SousDomaine (sous_domaine_id, f_domaine_id, nom_sous_domaine) VALUES (?, ?, ?)"
            cursor.execute(query, (sous_domaine_id, f_domaine_id, nom_sous_domaine))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_sous_domaine: {e}")

def insert_indicateur(indicateur_id, f_sous_domaine_id, nom_indicateur):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO Indicateur (indicateur_id, f_sous_domaine_id, nom_indicateur) VALUES (?, ?, ?)"
            cursor.execute(query, (indicateur_id, f_sous_domaine_id, nom_indicateur))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_indicateur: {e}")

def insert_sexe(sexe_id, sexe):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "INSERT INTO Sexe (sexe_id, sexe) VALUES (?, ?)"
            cursor.execute(query, (sexe_id, sexe))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_sexe: {e}")

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
