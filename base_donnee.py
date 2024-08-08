import sqlite3

conn = sqlite3.connect('annuiare.db')
cursor = conn.cursor()
#cursor.execute("DROP TABLE ValeursIndicateurs ")
#cursor.execute("DROP TABLE Departement")

import sqlite3

def create_tables():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('annuiare.db')
    cursor = conn.cursor()

    create_table_commands = [
        """
        CREATE TABLE IF NOT EXISTS DirectionStatistique (
            direction_id INTEGER PRIMARY KEY,
            Description TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Region (
            region_id INTEGER PRIMARY KEY,
            f_direction_stat_id INTEGER,
            nom_region TEXT,
            FOREIGN KEY (f_direction_stat_id) REFERENCES DirectionStatistique(direction_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Departement (
            departement_id INTEGER PRIMARY KEY,
            f_region_id INTEGER,
            nom_departement TEXT,
            FOREIGN KEY (f_region_id) REFERENCES Region(region_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS SousPrefectures (
            sousprefect_id INTEGER PRIMARY KEY,
            f_departement_id INTEGER,
            nom_sousprefecture TEXT,
            FOREIGN KEY (f_departement_id) REFERENCES Departement(departement_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Domaine (
            domaine_id INTEGER PRIMARY KEY,
            nom_domaine TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS SousDomaine (
            sous_domaine_id INTEGER PRIMARY KEY,
            f_domaine_id INTEGER,
            nom_sous_domaine TEXT,
            FOREIGN KEY (f_domaine_id) REFERENCES Domaine(domaine_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Indicateur (
            indicateur_id INTEGER PRIMARY KEY,
            f_domaine_id INTEGER,
            nom_indicateur TEXT,
            FOREIGN KEY (f_domaine_id) REFERENCES Domaine(domaine_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Sexe (
            sexe_id INTEGER PRIMARY KEY,
            sexe TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS GroupeAge (
            grp_age_id INTEGER PRIMARY KEY,
            groupe_age TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Age (
            age_id INTEGER PRIMARY KEY,
            age TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Directeur (
            id INTEGER PRIMARY KEY,
            Nom TEXT,
            Prenom TEXT,
            Email TEXT,
            Numero TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS AgentCollecte (
            id INTEGER PRIMARY KEY,
            Nom TEXT,
            Prenom TEXT,
            Email TEXT,
            Numero TEXT
        );
        """
    ]

    # Execute each create table command
    for command in create_table_commands:
        try:
            cursor.execute(command)
            print(f"Table créée avec succès avec la commande :\n{command}")
        except sqlite3.Error as e:
            print(f"Une erreur est survenue : {e.args[0]}")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the tables
create_tables()

def base_donne_condt_vie_menage(db_name):
    # Connexion à la base de données
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Liste des tables à créer
    tables = [
        "Cycle", "Niveau_Prescolaire", "Niveau_Primaire", "Niveau_Secondaire_1er_cycle",
        "Niveau_Secondaire_2nd_cycle", "Niveau_Technique", "Niveau_Superieur",
        "Niveau_Professionnel", "Type_examen", "Infrastructures_sanitaires",
        "Lieu_accouchement", "Etat_vaccinal", "Types_de_vaccination", "Pathologie",
        "Tranche_age", "Maladies_du_PEV", "Maladies_infectieuses", "Maladies_IST",
        "Type_de_Maladie", "Activites_IEC", "Service_Medicaux",
        "Type_infrastructures_ou_organisations_sportives", "Disciplines_sportives",
        "Type_infrastructures_culturelles", "Type_de_Patrimoines_culturels_immatériels",
        "Type_actions_culturelles_et_artistiques", "Type_operateurs_des_oeuvres_esprit",
        "Type_de_groupes_culturels", "Type_de_manifestations_culturelles"
    ]

    # Création des tables
    for table in tables:
        # Remplacez les espaces par des underscores pour les noms de tables
        table_name = table.replace(" ", "_")
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL
        );
        """
        cursor.execute(create_table_query)
        print(f"Table {table_name} créée avec succès.")

    # Fermeture de la connexion
    conn.commit()
    conn.close()
    print("Base de données créée et tables ajoutées avec succès.")

# Utilisation de la fonction
base_donne_condt_vie_menage('annuiare.db')

def create_valeurs_indicateurs_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS ValeursIndicateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        f_region_id INTEGER,
        f_departement_id INTEGER,
        f_sous_prefecture_id INTEGER,
        f_indicateur_id INTEGER,
        Valeur REAL,
        Annee INTEGER,
        f_sexe_id INTEGER,
        f_grp_age_id INTEGER,
        f_age_id INTEGER,
        f_cycle_id INTEGER,
        f_niveau_prescolaire_id INTEGER,
        f_niveau_primaire_id INTEGER,
        f_niveau_secondaire_1er_cycle_id INTEGER,
        f_niveau_secondaire_2nd_cycle_id INTEGER,
        f_niveau_technique_id INTEGER,
        f_niveau_superieur_id INTEGER,
        f_niveau_professionnel_id INTEGER,
        f_type_examen_id INTEGER,
        f_infrastructures_sanitaires_id INTEGER,
        f_lieu_accouchement_id INTEGER,
        f_etat_vaccinal_id INTEGER,
        f_types_de_vaccination_id INTEGER,
        f_pathologie_id INTEGER,
        f_tranche_age_id INTEGER,
        f_maladies_du_pev_id INTEGER,
        f_maladies_infectieuses_id INTEGER,
        f_maladies_ist_id INTEGER,
        f_type_de_maladie_id INTEGER,
        f_activites_iec_id INTEGER,
        f_service_medicaux_id INTEGER,
        f_type_infrastructures_ou_organisations_sportives_id INTEGER,
        f_disciplines_sportives_id INTEGER,
        f_type_infrastructures_culturelles_id INTEGER,
        f_type_de_patrimoines_culturels_immatériels_id INTEGER,
        f_type_actions_culturelles_et_artistiques_id INTEGER,
        f_type_operateurs_des_oeuvres_esprit_id INTEGER,
        f_type_de_groupes_culturels_id INTEGER,
        f_type_de_manifestations_culturelles_id INTEGER,
        FOREIGN KEY (f_region_id) REFERENCES Region(region_id),
        FOREIGN KEY (f_departement_id) REFERENCES Departement(departement_id),
        FOREIGN KEY (f_sous_prefecture_id) REFERENCES SousPrefectures(sousprefect_id),
        FOREIGN KEY (f_indicateur_id) REFERENCES Indicateur(indicateur_id),
        FOREIGN KEY (f_sexe_id) REFERENCES Sexe(sexe_id),
        FOREIGN KEY (f_grp_age_id) REFERENCES GroupeAge(grp_age_id),
        FOREIGN KEY (f_age_id) REFERENCES Age(age_id),
        FOREIGN KEY (f_cycle_id) REFERENCES Cycle(id),
        FOREIGN KEY (f_niveau_prescolaire_id) REFERENCES Niveau_Prescolaire(id),
        FOREIGN KEY (f_niveau_primaire_id) REFERENCES Niveau_Primaire(id),
        FOREIGN KEY (f_niveau_secondaire_1er_cycle_id) REFERENCES Niveau_Secondaire_1er_cycle(id),
        FOREIGN KEY (f_niveau_secondaire_2nd_cycle_id) REFERENCES Niveau_Secondaire_2nd_cycle(id),
        FOREIGN KEY (f_niveau_technique_id) REFERENCES Niveau_Technique(id),
        FOREIGN KEY (f_niveau_superieur_id) REFERENCES Niveau_Superieur(id),
        FOREIGN KEY (f_niveau_professionnel_id) REFERENCES Niveau_Professionnel(id),
        FOREIGN KEY (f_type_examen_id) REFERENCES Type_examen(id),
        FOREIGN KEY (f_infrastructures_sanitaires_id) REFERENCES Infrastructures_sanitaires(id),
        FOREIGN KEY (f_lieu_accouchement_id) REFERENCES Lieu_accouchement(id),
        FOREIGN KEY (f_etat_vaccinal_id) REFERENCES Etat_vaccinal(id),
        FOREIGN KEY (f_types_de_vaccination_id) REFERENCES Types_de_vaccination(id),
        FOREIGN KEY (f_pathologie_id) REFERENCES Pathologie(id),
        FOREIGN KEY (f_tranche_age_id) REFERENCES Tranche_age(id),
        FOREIGN KEY (f_maladies_du_pev_id) REFERENCES Maladies_du_pev(id),
        FOREIGN KEY (f_maladies_infectieuses_id) REFERENCES Maladies_infectieuses(id),
        FOREIGN KEY (f_maladies_ist_id) REFERENCES Maladies_ist(id),
        FOREIGN KEY (f_type_de_maladie_id) REFERENCES Type_de_Maladie(id),
        FOREIGN KEY (f_activites_iec_id) REFERENCES Activites_IEC(id),
        FOREIGN KEY (f_service_medicaux_id) REFERENCES Service_Medicaux(id),
        FOREIGN KEY (f_type_infrastructures_ou_organisations_sportives_id) REFERENCES Type_infrastructures_ou_organisations_sportives(id),
        FOREIGN KEY (f_disciplines_sportives_id) REFERENCES Disciplines_sportives(id),
        FOREIGN KEY (f_type_infrastructures_culturelles_id) REFERENCES Type_infrastructures_culturelles(id),
        FOREIGN KEY (f_type_de_patrimoines_culturels_immatériels_id) REFERENCES Type_de_Patrimoines_culturels_immatériels(id),
        FOREIGN KEY (f_type_actions_culturelles_et_artistiques_id) REFERENCES Type_actions_culturelles_et_artistiques(id),
        FOREIGN KEY (f_type_operateurs_des_oeuvres_esprit_id) REFERENCES Type_operateurs_des_oeuvres_esprit(id),
        FOREIGN KEY (f_type_de_groupes_culturels_id) REFERENCES Type_de_groupes_culturels(id),
        FOREIGN KEY (f_type_de_manifestations_culturelles_id) REFERENCES Type_de_manifestations_culturelles(id)
    );
    """
    cursor.execute(create_table_query)
    print("Table ValeursIndicateurs créée avec succès.")

    conn.commit()
    conn.close()
    print("Base de données mise à jour avec succès.")

create_valeurs_indicateurs_table('annuiare.db')
