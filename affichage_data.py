import sqlite3
import pandas as pd
import streamlit as st

# Fonction pour récupérer les données de la table ValeursIndicateurs
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

# Utilisation de Streamlit pour afficher les données
st.title("Valeurs Indicateurs")

df_valeurs_indicateurs = get_valeurs_indicateurs()

if not df_valeurs_indicateurs.empty:
    st.dataframe(df_valeurs_indicateurs)
else:
    st.write("No data available.")
