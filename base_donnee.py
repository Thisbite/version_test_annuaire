import sqlite3

conn = sqlite3.connect('annuiare.db')
cursor = conn.cursor()
#cursor.execute("DROP TABLE SousPrefectures ")
#cursor.execute("DROP TABLE Departement")




def create_tables():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('annuiare.db')
    cursor = conn.cursor()



    # SQL commands to create tables
    create_table_commands = [

        """
              CREATE TABLE IF NOT EXISTS DirectionStatistique (
                  direction_id INT PRIMARY KEY,
                  Description VARCHAR(255)
              );
              """,
        """
        CREATE TABLE IF NOT EXISTS Region (
            region_id INT PRIMARY KEY,
             f_direction_stat_id INT,
            nom_region VARCHAR(255),
            FOREIGN KEY (f_direction_stat_id) REFERENCES DirectionStatistique(direction_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Departement (
            departement_id INT PRIMARY KEY,
            f_region_id INT,
            nom_departement VARCHAR(255),
            FOREIGN KEY (f_region_id) REFERENCES Region(region_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS SousPrefectures (
            sousprefect_id INT PRIMARY KEY,
            f_departement_id INT,
            nom_sousprefecture VARCHAR(255),
            FOREIGN KEY (f_departement_id) REFERENCES Departement(departement_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Domaine (
            domaine_id INT PRIMARY KEY,
            nom_domaine VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS SousDomaine (
            sous_domaine_id INT PRIMARY KEY,
            f_domaine_id INT,
            nom_sous_domaine VARCHAR(255),
            FOREIGN KEY (f_domaine_id) REFERENCES Domaine(domaine_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Indicateur (
            indicateur_id INT PRIMARY KEY,
            f_domaine_id INT,
            nom_indicateur VARCHAR(255),
            FOREIGN KEY (f_domaine_id) REFERENCES Domaine(domaine_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Sexe (
            sexe_id INT PRIMARY KEY,
            sexe VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS GroupeAge (
            grp_age_id INT PRIMARY KEY,
            groupe_age VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Age (
            age_id INT PRIMARY KEY,
            age VARCHAR(255)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS Directeur (
            id INT PRIMARY KEY,
            Nom VARCHAR(255),
            Prenom VARCHAR(255),
            Email VARCHAR(255),
            Numero VARCHAR(20)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS AgentCollecte (
            id INT PRIMARY KEY,
            Nom VARCHAR(255),
            Prenom VARCHAR(255),
            Email VARCHAR(255),
            Numero VARCHAR(20)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ValeursIndicateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            f_region_id INT,
            f_departement_id INT,
            f_sous_prefecture_id INT,
            f_indicateur_id INT,
            Valeur DECIMAL(10, 2),
            Annee INT,
            f_sexe_id INT,
            f_grp_age_id INT,
            f_age_id INT,
            FOREIGN KEY (f_region_id) REFERENCES Region(region_id),
            FOREIGN KEY (f_departement_id) REFERENCES Departement(departement_id),
            FOREIGN KEY (f_sous_prefecture_id) REFERENCES SousPrefectures(sousprefect_id),
            FOREIGN KEY (f_indicateur_id) REFERENCES Indicateur(indicateur_id),
            FOREIGN KEY (f_sexe_id) REFERENCES Sexe(sexe_id),
            FOREIGN KEY (f_grp_age_id) REFERENCES GroupeAge(grp_age_id),
            FOREIGN KEY (f_age_id) REFERENCES Age(age_id)
        );
        """
    ]

    # Execute each create table command
    for command in create_table_commands:
        try:
            cursor.execute(command)
            print(f"Table created successfully with command:\n{command}")
        except sqlite3.Error as e:
            print(f"An error occurred: {e.args[0]}")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the tables
create_tables()
