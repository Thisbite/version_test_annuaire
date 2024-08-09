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


# Departement
df = pd.read_excel('departement.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Departement (departement_id, f_region_id , nom_departement) VALUES (?, ?, ?)",
                  (row['code_departement'], row['region_id'], row['departement']))



#Sous-préfecture
df = pd.read_excel('sous_prefecture.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO SousPrefectures(sousprefect_id, f_departement_id ,nom_sousprefecture) VALUES (?, ?, ?)",
                  (row['code_sous_prefecture'], row['departement_id'], row['sous_prefecture']))




# Domaine
df = pd.read_excel('domaine.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Domaine(domaine_id,nom_domaine) VALUES ( ?, ?)",
                  (row['code_domaine'], row['domaine']))



# Indicateurs
df = pd.read_excel('indicateurs.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Indicateur (indicateur_id ,f_domaine_id ,nom_indicateur ) VALUES (?, ?, ?)",
                  (row['code_indicateur'], row['domaine_id'], row['indicateur']))



#Direction statistique
df = pd.read_excel('direction_statistique.xlsx')

# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO DirectionStatistique(direction_id,Description) VALUES ( ?, ?)",
                  (row['code_direction'], row['description']))


#Sexe
df = pd.read_excel('sexe')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Sexe(sexe_id,sexe) VALUES ( ?, ?)",
                  (row['id'], row['sexe']))




conn.commit()

# Fermer la connexion
conn.close()


#Niveau préscolaire 
df = pd.read_excel('prescolaire.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Prescolaire(niv_prescolaire_id,nom_prescolaire) VALUES ( ?, ?)",
                  (row['id'], row['Niveau_Prescolaire']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



#Cycle
df = pd.read_excel('cycle.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Cycle(id_cycle,nom_cycle) VALUES ( ?, ?)",
                  (row['id'], row['Cycle']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()

"""





