import sqlite3

conn = sqlite3.connect('annuiare.db')
cursor = conn.cursor()
#cursor.execute("DROP TABLE ValeursIndicateurs ")


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


def nv_base():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('annuiare.db')
    cursor = conn.cursor()

    create_table_commands = [
        """
        CREATE TABLE IF NOT EXISTS Cycle (
            id_cycle INTEGER PRIMARY KEY,
            nom_cycle TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Prescolaire (
            niv_prescolaire_id INTEGER PRIMARY KEY,
            nom_prescolaire TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Primaire (
            niv_primaire_id INTEGER PRIMARY KEY,
            nom_primaire TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Secondaire_1er_cycle (
            niv_secondaire_1er_cycle_id INTEGER PRIMARY KEY,
            nom_secondaire_1er_cycle TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Secondaire_2nd_cycle (
            niv_secondaire_2nd_cycle_id INTEGER PRIMARY KEY,
            nom_secondaire_2nd_cycle TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Technique (
            niv_technique_id INTEGER PRIMARY KEY,
            nom_technique TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Superieur (
            niv_superieur_id INTEGER PRIMARY KEY,
            nom_superieur TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Niveau_Professionnel (
            niv_professionnel_id INTEGER PRIMARY KEY,
            nom_professionnel TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_examen (
            id_type_examen INTEGER PRIMARY KEY,
            nom_type_examen TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Infrastructures_sanitaires (
            id_infrastructures_sanitaires INTEGER PRIMARY KEY,
            nom_infrastructures_sanitaires TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Lieu_accouchement (
            id_lieu_accouchement INTEGER PRIMARY KEY,
            nom_lieu_accouchement TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Etat_vaccinal (
            id_etat_vaccinal INTEGER PRIMARY KEY,
            nom_etat_vaccinal TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Types_de_vaccination (
            id_types_de_vaccination INTEGER PRIMARY KEY,
            nom_types_de_vaccination TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Pathologie (
            id_pathologie INTEGER PRIMARY KEY,
            nom_pathologie TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Tranche_age (
            id_tranche_age INTEGER PRIMARY KEY,
            nom_tranche_age TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Maladies_du_PEV (
            id_maladies_du_pev INTEGER PRIMARY KEY,
            nom_maladies_du_pev TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Maladies_infectieuses (
            id_maladies_infectieuses INTEGER PRIMARY KEY,
            nom_maladies_infectieuses TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Infection_respiratoire (
                  id_infectieuses_respiratoire INTEGER PRIMARY KEY,
                  nom_infectieuses_respiratoire TEXT
              );
              """,
        """
        CREATE TABLE IF NOT EXISTS Maladies_IST (
            id_maladies_ist INTEGER PRIMARY KEY,
            nom_maladies_ist TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_Maladie (
            id_type_de_maladie INTEGER PRIMARY KEY,
            nom_type_de_maladie TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Activites_IEC (
            id_activites_iec INTEGER PRIMARY KEY,
            nom_activites_iec TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Service_Medicaux (
            id_service_medicaux INTEGER PRIMARY KEY,
            nom_service_medicaux TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_infrastructures_ou_organisations_sportives (
            id_type_infrastructures_sportives INTEGER PRIMARY KEY,
            nom_type_infrastructures_sportives TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Disciplines_sportives (
            id_disciplines_sportives INTEGER PRIMARY KEY,
            nom_disciplines_sportives TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_infrastructures_culturelles (
            id_type_infrastructures_culturelles INTEGER PRIMARY KEY,
            nom_type_infrastructures_culturelles TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_Patrimoines_culturels_immatériels (
            id_type_patrimoines_culturels_immatériels INTEGER PRIMARY KEY,
            nom_type_patrimoines_culturels_immatériels TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_actions_culturelles_et_artistiques (
            id_type_actions_culturelles_artistiques INTEGER PRIMARY KEY,
            nom_type_actions_culturelles_artistiques TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_operateurs_des_oeuvres_esprit (
            id_type_operateurs_oeuvres_esprit INTEGER PRIMARY KEY,
            nom_type_operateurs_oeuvres_esprit TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_groupes_culturels (
            id_type_groupes_culturels INTEGER PRIMARY KEY,
            nom_type_groupes_culturels TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Type_de_manifestations_culturelles (
            id_type_manifestations_culturelles INTEGER PRIMARY KEY,
            nom_type_manifestations_culturelles TEXT
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
"""
Exécution de la fonction 
"""

import sqlite3


import sqlite3

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
        f_infectieuses_respiratoire_id INTEGER,
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
        FOREIGN KEY (f_cycle_id) REFERENCES Cycle(id_cycle),
        FOREIGN KEY (f_niveau_prescolaire_id) REFERENCES Niveau_Prescolaire(niv_prescolaire_id),
        FOREIGN KEY (f_niveau_primaire_id) REFERENCES Niveau_Primaire(niv_primaire_id),
        FOREIGN KEY (f_niveau_secondaire_1er_cycle_id) REFERENCES Niveau_Secondaire_1er_cycle(niv_secondaire_1er_cycle_id),
        FOREIGN KEY (f_niveau_secondaire_2nd_cycle_id) REFERENCES Niveau_Secondaire_2nd_cycle(niv_secondaire_2nd_cycle_id),
        FOREIGN KEY (f_niveau_technique_id) REFERENCES Niveau_Technique(niv_technique_id),
        FOREIGN KEY (f_niveau_superieur_id) REFERENCES Niveau_Superieur(niv_superieur_id),
        FOREIGN KEY (f_niveau_professionnel_id) REFERENCES Niveau_Professionnel(niv_professionnel_id),
        FOREIGN KEY (f_type_examen_id) REFERENCES Type_examen(id_type_examen),
        FOREIGN KEY (f_infrastructures_sanitaires_id) REFERENCES Infrastructures_sanitaires(id_infrastructures_sanitaires),
        FOREIGN KEY (f_lieu_accouchement_id) REFERENCES Lieu_accouchement(id_lieu_accouchement),
        FOREIGN KEY (f_etat_vaccinal_id) REFERENCES Etat_vaccinal(id_etat_vaccinal),
        FOREIGN KEY (f_types_de_vaccination_id) REFERENCES Types_de_vaccination(id_types_de_vaccination),
        FOREIGN KEY (f_pathologie_id) REFERENCES Pathologie(id_pathologie),
        FOREIGN KEY (f_tranche_age_id) REFERENCES Tranche_age(id_tranche_age),
        FOREIGN KEY (f_maladies_du_pev_id) REFERENCES Maladies_du_PEV(id_maladies_du_pev),
        FOREIGN KEY (f_maladies_infectieuses_id) REFERENCES Maladies_infectieuses(id_maladies_infectieuses),
        FOREIGN KEY (f_infectieuses_respiratoire_id) REFERENCES Infection_respiratoire(id_infectieuses_respiratoire),
        FOREIGN KEY (f_maladies_ist_id) REFERENCES Maladies_IST(id_maladies_ist),
        FOREIGN KEY (f_type_de_maladie_id) REFERENCES Type_de_Maladie(id_type_de_maladie),
        FOREIGN KEY (f_activites_iec_id) REFERENCES Activites_IEC(id_activites_iec),
        FOREIGN KEY (f_service_medicaux_id) REFERENCES Service_Medicaux(id_service_medicaux),
        FOREIGN KEY (f_type_infrastructures_ou_organisations_sportives_id) REFERENCES Type_infrastructures_ou_organisations_sportives(id_type_infrastructures_sportives),
        FOREIGN KEY (f_disciplines_sportives_id) REFERENCES Disciplines_sportives(id_disciplines_sportives),
        FOREIGN KEY (f_type_infrastructures_culturelles_id) REFERENCES Type_infrastructures_culturelles(id_type_infrastructures_culturelles),
        FOREIGN KEY (f_type_de_patrimoines_culturels_immatériels_id) REFERENCES Type_de_Patrimoines_culturels_immatériels(id_type_patrimoines_culturels_immatériels),
        FOREIGN KEY (f_type_actions_culturelles_et_artistiques_id) REFERENCES Type_actions_culturelles_et_artistiques(id_type_actions_culturelles_artistiques),
        FOREIGN KEY (f_type_operateurs_des_oeuvres_esprit_id) REFERENCES Type_operateurs_des_oeuvres_esprit(id_type_operateurs_oeuvres_esprit),
        FOREIGN KEY (f_type_de_groupes_culturels_id) REFERENCES Type_de_groupes_culturels(id_type_groupes_culturels),
        FOREIGN KEY (f_type_de_manifestations_culturelles_id) REFERENCES Type_de_manifestations_culturelles(id_type_manifestations_culturelles)
    );
    """

    try:
        cursor.execute(create_table_query)
        print("Table ValeursIndicateurs créée avec succès.")
    except sqlite3.Error as e:
        print(f"Une erreur est survenue lors de la création de la table : {e.args[0]}")

    conn.commit()
    conn.close()
    print("Base de données mise à jour avec succès.")

create_tables()
# Les tables de désagrégation de condition de vie des ménages
nv_base()

# Appeler la fonction pour créer la table ValeursIndicateurs
create_valeurs_indicateurs_table('annuiare.db')


