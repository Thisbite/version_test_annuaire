import sqlite3
import pandas as pd

# Connexion à la base de données
conn = sqlite3.connect('/Users/mac/Desktop/ANNUAIRE/Version_2_annuaire/annuiare.db')
cursor = conn.cursor()

"""
#Region
df = pd.read_excel('region.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Region (region_id,f_direction_stat_id, nom_region ) VALUES (?, ?, ?)",
                  (row['code_region'], row['direction_id'], row['region']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


# Departement
df = pd.read_excel('departement.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Departement (departement_id, f_region_id , nom_departement) VALUES (?, ?, ?)",
                  (row['code_departement'], row['region_id'], row['departement']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()

#Sous-préfecture
df = pd.read_excel('sous_prefecture.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO SousPrefectures(sousprefect_id, f_departement_id ,nom_sousprefecture) VALUES (?, ?, ?)",
                  (row['code_sous_prefecture'], row['departement_id'], row['sous_prefecture']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Domaine
df = pd.read_excel('domaine.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Domaine(domaine_id,nom_domaine) VALUES ( ?, ?)",
                  (row['code_domaine'], row['domaine']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


# Indicateurs
df = pd.read_excel('indicateurs.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Indicateur (indicateur_id ,f_domaine_id ,nom_indicateur ) VALUES (?, ?, ?)",
                  (row['code_indicateur'], row['domaine_id'], row['indicateur']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


#Direction statistique
df = pd.read_excel('direction_statistique.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO DirectionStatistique(direction_id,Description) VALUES ( ?, ?)",
                  (row['code_direction'], row['description']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()

#Sexe
df = pd.read_excel('sexe')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Sexe(sexe_id,sexe) VALUES ( ?, ?)",
                  (row['id'], row['sexe']))

# Valider les modifications
conn.commit()


#Groupe d'âge 
"""






