import streamlit as st
import sqlite3
import pandas as pd


def get_db_connection():
    conn = sqlite3.connect('db_annuaire.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_indicateur_id(indicateur_name):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT indicateur_id FROM Indicateurs WHERE Titre = ?', (indicateur_name,))
    result = c.fetchone()
    conn.close()
    return result['indicateur_id'] if result else None


def check_table_structure():
    conn = sqlite3.connect('db_annuaire.db')
    c = conn.cursor()
    c.execute("PRAGMA table_info(Indicateurs);")
    columns = c.fetchall()
    conn.close()
    for column in columns:
        print(column)


def create_sample_data():
    conn = get_db_connection()
    c = conn.cursor()

    # Création des tables si elles n'existent pas
    c.execute('''
    CREATE TABLE IF NOT EXISTS Region (
        region_id INTEGER PRIMARY KEY,
        Description TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS Domaine (
        domaine_id INTEGER PRIMARY KEY,
        Description TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS SousDomaine (
        sousdomaine_id INTEGER PRIMARY KEY,
        domaine_id INTEGER,
        Description TEXT,
        FOREIGN KEY (domaine_id) REFERENCES Domaine(domaine_id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS Indicateurs (
        indicateur_id INTEGER PRIMARY KEY,
        sousdomaine_id INTEGER,
        Titre TEXT,
        FOREIGN KEY (sousdomaine_id) REFERENCES SousDomaine(sousdomaine_id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS Departement (
        departement_id INTEGER PRIMARY KEY,
        region_id INTEGER,
        Description TEXT,
        FOREIGN KEY (region_id) REFERENCES Region(region_id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS SousPrefectures (
        sousprefect_id INTEGER PRIMARY KEY,
        departement_id INTEGER,
        Description TEXT,
        FOREIGN KEY (departement_id) REFERENCES Departement(departement_id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS ValeursIndicateurs (
        val_indic_id INTEGER PRIMARY KEY,
        entite_geograph INTEGER,
        indicateur_id INTEGER,
        Valeur DECIMAL(10, 2),
        Annee INTEGER,
        sexe_id INTEGER,
        grpage_id INTEGER,
        age_id INTEGER,
        FOREIGN KEY (entite_geograph) REFERENCES EntiteGeographique(entite_geograph),
        FOREIGN KEY (indicateur_id) REFERENCES Indicateurs(indicateur_id),
        FOREIGN KEY (sexe_id) REFERENCES Sexe(sexe_id),
        FOREIGN KEY (grpage_id) REFERENCES GroupeAge(grpage_id),
        FOREIGN KEY (age_id) REFERENCES Age(age_id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS Sexe (
        sexe_id INTEGER PRIMARY KEY,
        Attributs TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS GroupeAge (
        grpage_id INTEGER PRIMARY KEY,
        Attributs TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS Age (
        age_id INTEGER PRIMARY KEY,
        Attributs TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS EntiteGeographique (
        entite_geograph INTEGER PRIMARY KEY,
        region_id INTEGER,
        departement_id INTEGER,
        sousprefect_id INTEGER,
        FOREIGN KEY (region_id) REFERENCES Region(region_id),
        FOREIGN KEY (departement_id) REFERENCES Departement(departement_id),
        FOREIGN KEY (sousprefect_id) REFERENCES SousPrefectures(sousprefect_id)
    )
    ''')

    # Insertion de données de test
    c.execute('INSERT OR IGNORE INTO Region (region_id, Description) VALUES (1, "Poro")')
    c.execute('INSERT OR IGNORE INTO Domaine (domaine_id, Description) VALUES (1, "Domaine1")')
    c.execute(
        'INSERT OR IGNORE INTO SousDomaine (sousdomaine_id, domaine_id, Description) VALUES (1, 1, "SousDomaine1")')
    c.execute('INSERT OR IGNORE INTO Indicateurs (indicateur_id, sousdomaine_id, Titre) VALUES (1, 1, "Indicateur1")')
    c.execute(
        'INSERT OR IGNORE INTO Departement (departement_id, region_id, Description) VALUES (1, 1, "Departement1")')
    c.execute(
        'INSERT OR IGNORE INTO SousPrefectures (sousprefect_id, departement_id, Description) VALUES (1, 1, "SousPrefecture1")')
    c.execute('INSERT OR IGNORE INTO Sexe (sexe_id, Attributs) VALUES (1, "M"), (2, "F")')
    c.execute('INSERT OR IGNORE INTO GroupeAge (grpage_id, Attributs) VALUES (1, "0-5"), (2, "6-10")')
    c.execute('INSERT OR IGNORE INTO Age (age_id, Attributs) VALUES (1, "0-5 ans"), (2, "6-10 ans")')
    c.execute(
        'INSERT OR IGNORE INTO EntiteGeographique (entite_geograph, region_id, departement_id, sousprefect_id) VALUES (1, 1, 1, 1)')
    c.execute(
        'INSERT OR IGNORE INTO ValeursIndicateurs (val_indic_id, entite_geograph, indicateur_id, Valeur, Annee, sexe_id, grpage_id, age_id) VALUES (1, 1, 1, 100.0, 2023, 1, 1, 1)')

    conn.commit()
    conn.close()


def afficher_donnees():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute('''
    SELECT 
        vi.val_indic_id, 
        r.Description as Region, 
        d.Description as Departement, 
        sp.Description as SousPrefecture,
        i.Titre as Indicateur,
        s.Attributs as Sexe, 
        ga.Attributs as GroupeAge, 
        a.Attributs as Age,
        vi.Valeur,
        vi.Annee

    FROM ValeursIndicateurs vi
    LEFT JOIN EntiteGeographique eg ON vi.entite_geograph = eg.entite_geograph
    LEFT JOIN Indicateurs i ON vi.indicateur_id = i.indicateur_id
    LEFT JOIN Sexe s ON vi.sexe_id = s.sexe_id
    LEFT JOIN GroupeAge ga ON vi.grpage_id = ga.grpage_id
    LEFT JOIN Age a ON vi.age_id = a.age_id
    LEFT JOIN Region r ON eg.region_id = r.region_id
    LEFT JOIN Departement d ON eg.departement_id = d.departement_id
    LEFT JOIN SousPrefectures sp ON eg.sousprefect_id = sp.sousprefect_id
    ''')

    data = c.fetchall()

    columns = ['ID', 'Région', 'Département', 'Sous-Préfecture', 'Indicateur', 'Sexe', 'Groupe d\'Âge', 'Âge', 'Valeur',
               'Année']
    df = pd.DataFrame(data, columns=columns)

    st.dataframe(df)

    conn.close()


def test():
    st.title("Saisie des données d'indicateurs")

    # Liste des indicateurs (exemple statique ici, pourrait être dynamique aussi)
    indicateur_names = [
        "Indicateur1",
        "Nombre de personnel médical et paramédical",
        "Autre indicateur"
    ]
    indicateur = st.selectbox("Sélectionner Indicateur", indicateur_names)

    # Créer le formulaire
    with st.form("formulaire_saisie_donnees"):
        region = st.selectbox("Sélectionner Région", [" ", "Poro", "Autre région"], index=0)
        departement = st.text_input("Département", value="-")
        sexe = st.selectbox("Sexe", [" ", "M", "F"], index=0)
        valeur_indicateur = st.number_input("Valeur de l'Indicateur", min_value=0.0, value=0.0, format="%f")

        # Dynamically show additional fields based on the selected indicator
        if indicateur == "Indicateur1":
            type_personne_medical = st.selectbox("Type de personne médical", ["Médecin", "Infirmier"], index=0)

        soumis = st.form_submit_button("Soumettre")

        if soumis:
            indicateur_id = get_indicateur_id(indicateur)
            if indicateur_id:
                conn = get_db_connection()
                c = conn.cursor()

                # Insert data dynamically based on the selected indicator
                c.execute('''
                    INSERT INTO ValeursIndicateurs (entite_geograph, indicateur_id, Valeur, Annee, sexe_id, grpage_id, age_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (region, indicateur_id, valeur_indicateur, 2023, sexe, None, None))

                # Insert into NiveauDeDesagregation if applicable
                if indicateur == "Indicateur1":
                    c.execute('''
                        INSERT INTO NiveauDeDesagregation (sexe_id, grpage_id, age_id, val_indic_id)
                        VALUES (?, ?, ?, ?)
                    ''', (sexe, None, None, c.lastrowid))

                conn.commit()
                conn.close()
                st.success("Données soumises avec succès")
            else:
                st.error("Indicateur non trouvé")


# Appel des fonctions dans l'application Streamlit
st.title('Affichage des Données')
create_sample_data()
afficher_donnees()

# Exécuter l'application Streamlit
if __name__ == "__main__":
    test()
    check_table_structure()
