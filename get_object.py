import sqlite3
import pandas as pd
import streamlit as st
def get_indicators(domaine_id=None):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            if domaine_id is not None:
                query = "SELECT indicateur_id, nom_indicateur FROM Indicateur WHERE f_domaine_id = ? ORDER BY nom_indicateur"
                cursor.execute(query, (domaine_id,))
            else:
                query = "SELECT indicateur_id, nom_indicateur FROM Indicateur"
                cursor.execute(query)
            indicators = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_indicators: {e}")
        return []
    return indicators


def get_sexes():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT sexe_id, sexe FROM Sexe")
            sexes = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_sexes: {e}")
        return []
    return sexes

def get_groue_age():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT grp_age_id, groupe_age FROM GroupeAge")
            groupe_age = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_groue_age: {e}")
        return []
    return groupe_age

def get_regions():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT region_id, nom_region FROM Region")
            regions = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_regions: {e}")
        return []
    return regions

def get_departments(selected_region):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "SELECT departement_id, nom_departement FROM Departement WHERE f_region_id = ?"
            cursor.execute(query, (selected_region,))
            departments = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_departments: {e}")
        return []
    return departments

def get_sous_prefectures(selected_department):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "SELECT sousprefect_id, nom_sousprefecture FROM SousPrefectures WHERE f_departement_id = ?"
            cursor.execute(query, (selected_department,))
            sousprefectures = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_sous_prefectures: {e}")
        return []
    return sousprefectures


def get_region_name(region_code):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "SELECT nom_region FROM Region WHERE region_id = ?"
            cursor.execute(query, (region_code,))
            region_name = cursor.fetchone()
            if region_name:
                return region_name[0]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Exception in get_region_name: {e}")
        return None

def get_department_name(department_code):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "SELECT nom_departement FROM Departement WHERE departement_id = ?"
            cursor.execute(query, (department_code,))
            department_name = cursor.fetchone()
            if department_name:
                return department_name[0]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Exception in get_department_name: {e}")
        return None

def get_sous_prefecture_name(sous_prefecture_code):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            query = "SELECT nom_sousprefecture FROM SousPrefectures WHERE sousprefect_id = ?"
            cursor.execute(query, (sous_prefecture_code,))
            sous_prefecture_name = cursor.fetchone()
            if sous_prefecture_name:
                return sous_prefecture_name[0]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Exception in get_sous_prefecture_name: {e}")
        return None








def get_geographical_entity_name(code_entite):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()

            # Recherche dans la table Region
            cursor.execute("SELECT nom_region FROM Region WHERE region_id = ?", (code_entite,))
            result = cursor.fetchone()
            if result:
                return "Region", result[0]

            # Recherche dans la table Departement
            cursor.execute("SELECT nom_departement FROM Departement WHERE departement_id = ?", (code_entite,))
            result = cursor.fetchone()
            if result:
                return "Departement", result[0]

            # Recherche dans la table SousPrefectures
            cursor.execute("SELECT nom_sousprefecture FROM SousPrefectures WHERE sousprefect_id = ?", (code_entite,))
            result = cursor.fetchone()
            if result:
                return "SousPrefecture", result[0]

            return None, None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None, None
    except Exception as e:
        print(f"Exception in get_geographical_entity_name: {e}")
        return None, None




"""
Section insection des données te affichage des données
"""

def get_valeurs_indicateurs():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            query = """
            SELECT 
                vi.id, 
                COALESCE(r.nom_region, r2.nom_region, r3.nom_region) AS nom_region, 
                COALESCE(d.nom_departement, d2.nom_departement) AS nom_departement, 
                sp.nom_sousprefecture, 
                i.nom_indicateur, 
                vi.Valeur, 
                vi.Annee, 
                s.sexe, 
                ga.groupe_age, 
                a.age
            FROM 
                ValeursIndicateurs vi
                LEFT JOIN Region r ON vi.f_region_id = r.region_id
                LEFT JOIN Departement d ON vi.f_departement_id = d.departement_id
                LEFT JOIN SousPrefectures sp ON vi.f_sous_prefecture_id = sp.sousprefect_id
                LEFT JOIN Indicateur i ON vi.f_indicateur_id = i.indicateur_id
                LEFT JOIN Sexe s ON vi.f_sexe_id = s.sexe_id
                LEFT JOIN GroupeAge ga ON vi.f_grp_age_id = ga.grp_age_id
                LEFT JOIN Age a ON vi.f_age_id = a.age_id
                LEFT JOIN Departement d2 ON sp.f_departement_id = d2.departement_id
                LEFT JOIN Region r2 ON d2.f_region_id = r2.region_id
                LEFT JOIN Region r3 ON d.f_region_id = r3.region_id
            """
            df = pd.read_sql(query, conn)
    except sqlite3.Error as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Exception in get_valeurs_indicateurs: {e}")
        return pd.DataFrame()
    return df
def insert_value(indicator_id, region_id, department_id, sous_prefecture_id, sexe_id, valeur, annee, groupe_age_id):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO ValeursIndicateurs (f_region_id, f_departement_id, f_sous_prefecture_id, f_indicateur_id, 
                                                f_sexe_id, Valeur, Annee, f_cycle_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (region_id, department_id, sous_prefecture_id, indicator_id, sexe_id, valeur, annee, groupe_age_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_value: {e}")