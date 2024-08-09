import sqlite3

import pandas as pd


def afficher_valeurs_indicateurs(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = """
    SELECT 
        VI.id,
        R.nom_region,
        D.nom_departement,
        SP.nom_sousprefecture,
        I.nom_indicateur,
        VI.Valeur,
        VI.Annee,
        S.sexe,
        GA.groupe_age,
        A.age,
        C.nom_cycle,
        NP.nom_prescolaire,
        N1C.nom_primaire,
        NS1C.nom_secondaire_1er_cycle ,
       NS2C.nom_secondaire_2nd_cycle,
       
        NT.nom_technique,
        NS.nom_superieur,
        NP.nom_professionnel,
        TE.nom_type_examen,
        SIS.nom_infrastructures_sanitaires,
        LA.nom_lieu_accouchement,
        EV.nom_etat_vaccinal,
        TV.nom_types_de_vaccination,
        P.nom_pathologie,
        TA.nom_tranche_age,
        MP.nom_maladies_du_pev,
        MI.nom_maladies_infectieuses,
        IST.nom_maladies_ist,
        TM.nom_type_de_maladie,
        AI.nom_activites_iec,
        SM.nom_service_medicaux,
        TIS.nom_type_infrastructures_sportives,
        DS.nom_disciplines_sportives,
        TIC.nom_type_infrastructures_culturelles,
        PCI.nom_type_patrimoines_culturels_immatériels,
        ACA.nom_type_actions_culturelles_artistiques,
        OE.nom_type_operateurs_oeuvres_esprit,
        GC.nom_type_groupes_culturels,
        MC.nom_type_manifestations_culturelles
    FROM ValeursIndicateurs VI
    LEFT JOIN Region R ON VI.f_region_id = R.region_id
    LEFT JOIN Departement D ON VI.f_departement_id = D.departement_id
    LEFT JOIN SousPrefectures SP ON VI.f_sous_prefecture_id = SP.sousprefect_id
    LEFT JOIN Indicateur I ON VI.f_indicateur_id = I.indicateur_id
    LEFT JOIN Sexe S ON VI.f_sexe_id = S.sexe_id
    LEFT JOIN GroupeAge GA ON VI.f_grp_age_id = GA.grp_age_id
    LEFT JOIN Age A ON VI.f_age_id = A.age_id
    LEFT JOIN Cycle C ON VI.f_cycle_id = C.id_cycle
    LEFT JOIN Niveau_Prescolaire NP ON VI.f_niveau_prescolaire_id = NP.niv_prescolaire_id
    LEFT JOIN Niveau_Primaire N1C ON VI.f_niveau_primaire_id = N1C.niv_primaire_id
    LEFT JOIN Niveau_Secondaire_1er_cycle NS1C ON VI.f_niveau_secondaire_1er_cycle_id = NS1C.niv_secondaire_1er_cycle_id
    LEFT JOIN Niveau_Secondaire_2nd_cycle NS2C ON VI.f_niveau_secondaire_2nd_cycle_id = NS2C.niv_secondaire_2nd_cycle_id
    LEFT JOIN Niveau_Technique NT ON VI.f_niveau_technique_id = NT.niv_technique_id
    LEFT JOIN Niveau_Superieur NS ON VI.f_niveau_superieur_id = NS.niv_superieur_id
    LEFT JOIN Niveau_Professionnel NP ON VI.f_niveau_professionnel_id = NP.niv_professionnel_id
    LEFT JOIN Type_examen TE ON VI.f_type_examen_id = TE.id_type_examen
    LEFT JOIN Infrastructures_sanitaires SIS ON VI.f_infrastructures_sanitaires_id = SIS.id_infrastructures_sanitaires
    LEFT JOIN Lieu_accouchement LA ON VI.f_lieu_accouchement_id = LA.id_lieu_accouchement
    LEFT JOIN Etat_vaccinal EV ON VI.f_etat_vaccinal_id = EV.id_etat_vaccinal
    LEFT JOIN Types_de_vaccination TV ON VI.f_types_de_vaccination_id = TV.id_types_de_vaccination
    LEFT JOIN Pathologie P ON VI.f_pathologie_id = P.id_pathologie
    LEFT JOIN Tranche_age TA ON VI.f_tranche_age_id = TA.id_tranche_age
    LEFT JOIN Maladies_du_PEV MP ON VI.f_maladies_du_pev_id = MP.id_maladies_du_pev
    LEFT JOIN Maladies_infectieuses MI ON VI.f_maladies_infectieuses_id = MI.id_maladies_infectieuses
    LEFT JOIN Maladies_IST IST ON VI.f_maladies_ist_id = IST.id_maladies_ist
    LEFT JOIN Type_de_Maladie TM ON VI.f_type_de_maladie_id = TM.id_type_de_maladie
    LEFT JOIN Activites_IEC AI ON VI.f_activites_iec_id = AI.id_activites_iec
    LEFT JOIN Service_Medicaux SM ON VI.f_service_medicaux_id = SM.id_service_medicaux
    LEFT JOIN Type_infrastructures_ou_organisations_sportives TIS ON VI.f_type_infrastructures_ou_organisations_sportives_id = TIS.id_type_infrastructures_sportives
    LEFT JOIN Disciplines_sportives DS ON VI.f_disciplines_sportives_id = DS.id_disciplines_sportives
    LEFT JOIN Type_infrastructures_culturelles TIC ON VI.f_type_infrastructures_culturelles_id = TIC.id_type_infrastructures_culturelles
    LEFT JOIN Type_de_Patrimoines_culturels_immatériels PCI ON VI.f_type_de_patrimoines_culturels_immatériels_id = PCI.id_type_patrimoines_culturels_immatériels
    LEFT JOIN Type_actions_culturelles_et_artistiques ACA ON VI.f_type_actions_culturelles_et_artistiques_id = ACA.id_type_actions_culturelles_artistiques
    LEFT JOIN Type_operateurs_des_oeuvres_esprit OE ON VI.f_type_operateurs_des_oeuvres_esprit_id = OE.id_type_operateurs_oeuvres_esprit
    LEFT JOIN Type_de_groupes_culturels GC ON VI.f_type_de_groupes_culturels_id = GC.id_type_groupes_culturels
    LEFT JOIN Type_de_manifestations_culturelles MC ON VI.f_type_de_manifestations_culturelles_id = MC.id_type_manifestations_culturelles
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    df=pd.DataFrame(rows,columns=["ID",
"Région",
"Département",
"Sous-préfecture",
"Indicateur",
"Valeur Indicateur",
"Année de collecte",
"Sexe",
"Groupe d'âge",
"Age",
"Cycle scolaire",
"Niveau préscolaire",
"Niveau primaire",
"Niveau Secondaire 1er cycle",
"Niveau Secondaire 2nd cycle",
"Niveau Technique",
"Niveau Supérieur",
"Niveau Professionnel",
"Type d'examen",
"Infrastructures sanitaires",
"Lieu d'accouchement",
"État vaccinal",
"Types de vaccination",
"Pathologie",
"Tranche d'âge",
"Maladies du PEV",
"Maladies infectieuses",
"Maladies IST",
"Type de maladie",
"Activités IEC",
"Services médicaux",
"Type d'infrastructures sportives",
"Disciplines sportives",
"Type d'infrastructures culturelles",
"Type de patrimoines culturels immatériels",
"Type d'actions culturelles et artistiques",
"Type d'opérateurs des œuvres d'esprit",
"Type de groupes culturels",
"Type de manifestations culturelles"
])

    conn.close()
    return df

# Appel de la fonction pour afficher les données
df=afficher_valeurs_indicateurs('annuiare.db')

