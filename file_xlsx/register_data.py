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
df = pd.read_excel('sexe_ok.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Sexe(sexe_id,sexe) VALUES ( ?, ?)",
                  (row['id'], row['nom']))




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


#Primaire
df = pd.read_excel('primaire_ds')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Primaire(niv_primaire_id,nom_primaire) VALUES ( ?, ?)",
                  (row['id'], row['primaire']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


#Niveau secondaire premier cycle
df = pd.read_excel('second_1er_cycle.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Secondaire_1er_cycle( niv_secondaire_1er_cycle_id, nom_secondaire_1er_cycle) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



#Niveau secondaire 2eme cyle
df = pd.read_excel('niveau_secon_2nd_cycle.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Secondaire_2nd_cycle(niv_secondaire_2nd_cycle_id,nom_secondaire_2nd_cycle) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()




#Niveau technique
df = pd.read_excel('niveau_technique.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Technique(niv_technique_id,nom_technique) VALUES ( ?, ?)",
                  (row['id'], row['niveau_technique']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


#Supérieur cycle
df = pd.read_excel('superieur_cycle.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Superieur( niv_superieur_id, nom_superieur) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



#Proffessionnelle cycle
df = pd.read_excel('professionnelle_cycle.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Niveau_Professionnel( niv_professionnel_id, nom_professionnel) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



#type examen
df = pd.read_excel('examen_scolaire.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Type_examen( id_type_examen, nom_type_examen) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()

#Groupe age
df = pd.read_excel('groupe_age')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO  GroupeAge ( grp_age_id,  groupe_age ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


#Infractructure sanitaire
df = pd.read_excel('infrastructure_sani.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO  Infrastructures_sanitaires ( id_infrastructures_sanitaires,  nom_infrastructures_sanitaires ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Lieu Accouchement
df = pd.read_excel('accouchement.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO  Lieu_accouchement ( id_lieu_accouchement,  nom_lieu_accouchement ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Services médicaux
df = pd.read_excel('service_medicaux.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Service_Medicaux( id_service_medicaux,  nom_service_medicaux ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()




# Etat de vaccination
df = pd.read_excel('etat_vaccination.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Etat_vaccinal( id_etat_vaccinal,  nom_etat_vaccinal ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()

# Type de vaccination 
df = pd.read_excel('type_vaccination.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Types_de_vaccination( id_types_de_vaccination,  nom_types_de_vaccination ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Pathologie
df = pd.read_excel('pathologie.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Pathologie( id_pathologie,  nom_pathologie ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Tranche d'âge
df = pd.read_excel('tranche_age.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Tranche_age( id_tranche_age,  nom_tranche_age ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Maladie PEV
df = pd.read_excel('maladie_pev.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Maladies_du_PEV( id_maladies_du_pev,  nom_maladies_du_pev ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Maladie infectieuse
df = pd.read_excel('maladies_infectieuse.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Maladies_infectieuses( id_maladies_infectieuses, nom_maladies_infectieuses ) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


#Infections respiratoire
df = pd.read_excel('infection_respiratoire.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Infection_respiratoire( id_infectieuses_respiratoire,nom_infectieuses_respiratoire) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



#Maladies IST
df = pd.read_excel('maladie_ist.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Maladies_IST( id_maladies_ist,nom_maladies_ist) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



# Type maladies
df = pd.read_excel('type_maladie.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Type_de_Maladie( id_type_de_maladie,nom_type_de_maladie) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()


# Activités IES
df = pd.read_excel('activite_ies.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Activites_IEC( id_activites_iec,nom_activites_iec) VALUES ( ?, ?)",
                  (row['id'], row['nom']))

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()

#Sexe
df = pd.read_excel('ok_sexe.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Sexe(sexe_id,sexe) VALUES ( ?, ?)",
                  (row['id'], row['nom']))
conn.commit()
conn.close()


"""
#Trimestre
df = pd.read_excel('trimestre.xlsx')
# Insertion des données par blocs (plus efficace)
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Trimestre VALUES ( ?, ?)",
                  (row['id'], row['nom']))
conn.commit()
conn.close()









