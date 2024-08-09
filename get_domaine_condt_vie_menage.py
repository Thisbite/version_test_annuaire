
import sqlite3

def get_cycle():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_cycle, nom_cycle FROM Cycle")
            cycles = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_cycle: {e}")
        return []
    return cycles

def get_niveau_prescolaire():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT niv_prescolaire_id, nom_prescolaire FROM Niveau_Prescolaire")
            niveaux_prescolaires = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_prescolaire: {e}")
        return []
    return niveaux_prescolaires

def get_niveau_primaire():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Niveau_Primaire")
            niveaux_primaires = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_primaire: {e}")
        return []
    return niveaux_primaires

def get_niveau_secondaire_1er_cycle():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Niveau_Secondaire_1er_cycle")
            niveaux_secondaires_1er_cycle = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_secondaire_1er_cycle: {e}")
        return []
    return niveaux_secondaires_1er_cycle

def get_niveau_secondaire_2nd_cycle():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Niveau_Secondaire_2nd_cycle")
            niveaux_secondaires_2nd_cycle = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_secondaire_2nd_cycle: {e}")
        return []
    return niveaux_secondaires_2nd_cycle

def get_niveau_technique():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Niveau_Technique")
            niveaux_techniques = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_technique: {e}")
        return []
    return niveaux_techniques

def get_niveau_superieur():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Niveau_Superieur")
            niveaux_superieurs = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_superieur: {e}")
        return []
    return niveaux_superieurs

def get_niveau_professionnel():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Niveau_Professionnel")
            niveaux_professionnels = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_niveau_professionnel: {e}")
        return []
    return niveaux_professionnels

def get_type_examen():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Type_examen")
            types_examens = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_examen: {e}")
        return []
    return types_examens

def get_infrastructures_sanitaires():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Infrastructures_sanitaires")
            infrastructures_sanitaires = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_infrastructures_sanitaires: {e}")
        return []
    return infrastructures_sanitaires

def get_lieu_accouchement():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Lieu_accouchement")
            lieux_accouchement = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_lieu_accouchement: {e}")
        return []
    return lieux_accouchement

def get_etat_vaccinal():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Etat_vaccinal")
            etats_vaccinaux = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_etat_vaccinal: {e}")
        return []
    return etats_vaccinaux

def get_types_de_vaccination():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Types_de_vaccination")
            types_de_vaccination = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_types_de_vaccination: {e}")
        return []
    return types_de_vaccination

def get_pathologie():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Pathologie")
            pathologies = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_pathologie: {e}")
        return []
    return pathologies

def get_tranche_age():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Tranche_age")
            tranches_age = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_tranche_age: {e}")
        return []
    return tranches_age

def get_maladies_du_pev():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Maladies_du_pev")
            maladies_du_pev = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_maladies_du_pev: {e}")
        return []
    return maladies_du_pev

def get_maladies_infectieuses():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Maladies_infectieuses")
            maladies_infectieuses = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_maladies_infectieuses: {e}")
        return []
    return maladies_infectieuses

def get_maladies_ist():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Maladies_ist")
            maladies_ist = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_maladies_ist: {e}")
        return []
    return maladies_ist

def get_type_de_maladie():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Type_de_Maladie")
            types_de_maladie = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_de_maladie: {e}")
        return []
    return types_de_maladie

def get_activites_iec():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Activites_IEC")
            activites_iec = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_activites_iec: {e}")
        return []
    return activites_iec

def get_service_medicaux():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Service_Medicaux")
            services_medicaux = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_service_medicaux: {e}")
        return []
    return services_medicaux

def get_type_infrastructures_ou_organisations_sportives():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Type_infrastructures_ou_organisations_sportives")
            types_infrastructures_ou_organisations_sportives = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_infrastructures_ou_organisations_sportives: {e}")
        return []
    return types_infrastructures_ou_organisations_sportives

def get_disciplines_sportives():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Disciplines_sportives")
            disciplines_sportives = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_disciplines_sportives: {e}")
        return []
    return disciplines_sportives

def get_type_infrastructures_culturelles():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Type_infrastructures_culturelles")
            types_infrastructures_culturelles = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_infrastructures_culturelles: {e}")
        return []
    return types_infrastructures_culturelles

def get_type_de_patrimoines_culturels_immatériels():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Type_de_Patrimoines_culturels_immatériels")
            types_patrimoines_culturels_immatériels = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_de_patrimoines_culturels_immatériels: {e}")
        return []
    return types_patrimoines_culturels_immatériels

def get_type_actions_culturelles_et_artistiques():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Type_actions_culturelles_et_artistiques")
            types_actions_culturelles_et_artistiques = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_actions_culturelles_et_artistiques: {e}")
        return []
    return types_actions_culturelles_et_artistiques

def get_type_operateurs_des_oeuvres_esprit():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Type_operateurs_des_oeuvres_esprit")
            types_operateurs_des_oeuvres_esprit = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_operateurs_des_oeuvres_esprit: {e}")
        return []
    return types_operateurs_des_oeuvres_esprit

def get_type_de_groupes_culturels():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Type_de_groupes_culturels")
            types_groupes_culturels = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_de_groupes_culturels: {e}")
        return []
    return types_groupes_culturels

def get_type_de_manifestations_culturelles():
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nom FROM Type_de_manifestations_culturelles")
            types_manifestations_culturelles = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Exception in get_type_de_manifestations_culturelles: {e}")
        return []
    return types_manifestations_culturelles





import sqlite3

def insert_value_cdt_vie(indicator_id, region_id, department_id, sous_prefecture_id, sexe_id, valeur, annee,
                         groupe_age_id=None, age_id=None, cycle_id=None, niveau_prescolaire_id=None,
                         niveau_primaire_id=None, niveau_secondaire_1er_cycle_id=None, niveau_secondaire_2nd_cycle_id=None,
                         niveau_technique_id=None, niveau_superieur_id=None, niveau_professionnel_id=None,
                         type_examen_id=None, infrastructures_sanitaires_id=None, lieu_accouchement_id=None,
                         etat_vaccinal_id=None, types_de_vaccination_id=None, pathologie_id=None,
                         tranche_age_id=None, maladies_du_pev_id=None, maladies_infectieuses_id=None,
                         maladies_ist_id=None, type_de_maladie_id=None, activites_iec_id=None,
                         service_medicaux_id=None, type_infrastructures_ou_organisations_sportives_id=None,
                         disciplines_sportives_id=None, type_infrastructures_culturelles_id=None,
                         type_de_patrimoines_culturels_immatériels_id=None, type_actions_culturelles_et_artistiques_id=None,
                         type_operateurs_des_oeuvres_esprit_id=None, type_de_groupes_culturels_id=None,
                         type_de_manifestations_culturelles_id=None):
    try:
        with sqlite3.connect('annuiare.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO ValeursIndicateurs (
                    f_region_id, f_departement_id, f_sous_prefecture_id, f_indicateur_id, f_sexe_id, Valeur, Annee,
                    f_grp_age_id, f_age_id, f_cycle_id, f_niveau_prescolaire_id, f_niveau_primaire_id,
                    f_niveau_secondaire_1er_cycle_id, f_niveau_secondaire_2nd_cycle_id, f_niveau_technique_id,
                    f_niveau_superieur_id, f_niveau_professionnel_id, f_type_examen_id, f_infrastructures_sanitaires_id,
                    f_lieu_accouchement_id, f_etat_vaccinal_id, f_types_de_vaccination_id, f_pathologie_id,
                    f_tranche_age_id, f_maladies_du_pev_id, f_maladies_infectieuses_id, f_maladies_ist_id,
                    f_type_de_maladie_id, f_activites_iec_id, f_service_medicaux_id,
                    f_type_infrastructures_ou_organisations_sportives_id, f_disciplines_sportives_id,
                    f_type_infrastructures_culturelles_id, f_type_de_patrimoines_culturels_immatériels_id,
                    f_type_actions_culturelles_et_artistiques_id, f_type_operateurs_des_oeuvres_esprit_id,
                    f_type_de_groupes_culturels_id, f_type_de_manifestations_culturelles_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (region_id, department_id, sous_prefecture_id, indicator_id, sexe_id, valeur, annee,
                  groupe_age_id, age_id, cycle_id, niveau_prescolaire_id, niveau_primaire_id, niveau_secondaire_1er_cycle_id,
                  niveau_secondaire_2nd_cycle_id, niveau_technique_id, niveau_superieur_id, niveau_professionnel_id,
                  type_examen_id, infrastructures_sanitaires_id, lieu_accouchement_id, etat_vaccinal_id,
                  types_de_vaccination_id, pathologie_id, tranche_age_id, maladies_du_pev_id, maladies_infectieuses_id,
                  maladies_ist_id, type_de_maladie_id, activites_iec_id, service_medicaux_id,
                  type_infrastructures_ou_organisations_sportives_id, disciplines_sportives_id,
                  type_infrastructures_culturelles_id, type_de_patrimoines_culturels_immatériels_id,
                  type_actions_culturelles_et_artistiques_id, type_operateurs_des_oeuvres_esprit_id,
                  type_de_groupes_culturels_id, type_de_manifestations_culturelles_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_value_cdt_vie: {e}")

