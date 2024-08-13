import streamlit as st
import get_object as go
import get_domaine_condt_vie_menage as g_vie

st.set_page_config(page_title="Formulaire de collecte", page_icon="📊")
# Injecter le CSS Bootstrap et le style personnalisé
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
    
        .custom-bold-text {
            font-weight: bold;
            color: black;
            font-size: 45px; 
        }
      
       
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
    .stButton button {
        background-color: orange;
        color: white;
        display: block;
        margin: 0 auto;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    textarea {
        font-size: 1.3rem !important;
    }
    input {
        font-size: 1.3rem !important;
    }
    .label{
     font-size: 1.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .custom-label {
        font-size: 1.2rem;

        color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)




def dom_condt_vie_menage():
    st.markdown("<h2 class='text-center text-primary custom-bold-text'>Formulaire de collecte</h2>",
                unsafe_allow_html=True)

    # Entrée du code d'entité géographique avec le cadre bleu
    with st.expander("Cliquer ici ",expanded=True):


        st.markdown('<p class="custom-label">Année de collecte</p>', unsafe_allow_html=True)
        annee = st.number_input('', min_value=2000, max_value=2100, step=1, key="year_g",label_visibility='hidden')

        st.markdown('<p class="custom-label">Saisie le code de l\'entité géographique</p>', unsafe_allow_html=True)
        code_entite = st.number_input('', min_value=0, step=1,label_visibility='hidden')

        entity_type, entity_name = go.get_geographical_entity_name(code_entite)
        if entity_type and entity_name:
            st.markdown(f'<p class="custom-label">Entité géographique : {entity_type}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="custom-label">Nom : {entity_name}</p>', unsafe_allow_html=True)



        region_id = None
        department_id = None
        sous_prefecture_id = None

        # Pour récupérer le code entité géographique
        if go.get_region_name(code_entite):
            region_id = code_entite
        elif go.get_department_name(code_entite):
            department_id = code_entite
        elif go.get_sous_prefecture_name(code_entite):
            sous_prefecture_id = code_entite

        # Section indicateur
        st.markdown('<p class="custom-label">Entrez le code indicateur</p>', unsafe_allow_html=True)
        ind = st.number_input(" ", min_value=0, step=1,key="ind1",label_visibility='hidden')
        indicator = go.get_indicators(ind)


        level_of_disaggregation = None  # Initialize with None

        if indicator:
            id_indicateur, nom_indicateur = indicator

            st.markdown(f'<p class="custom-label">Indicateur : {nom_indicateur}</p>', unsafe_allow_html=True)

            if 2001 <= id_indicateur <= 2029:

                st.markdown('<p class="custom-label">Choisir le niveau désagrégation</p>', unsafe_allow_html=True)

                desagration_list = ["",  "Cycle","Niveau préscolaire", "Niveau primaire", "Niveau Secondaire 1er cycle",
                                    "Niveau Secondaire 2nd cycle", "Niveau Technique", "Niveau Supérieur",
                                    "Niveau Professionnel",
                                     "Type d'examen","Sexe"]

                level_of_disaggregation = st.selectbox(" ", desagration_list, label_visibility='hidden')
            elif 1001 <= id_indicateur <= 1024:
                st.write("---------------------")
                st.markdown('<p class="custom-label">Choisir le niveau désagrégation</p>', unsafe_allow_html=True)

                desagration_list = ["","Sexe", "Groupe d'âge"]

                level_of_disaggregation = st.selectbox(" ", desagration_list, label_visibility='hidden')


            elif 2030<= id_indicateur <= 2102:
                st.write("---------------------")
                st.markdown('<p class="custom-label"> Niveau désagrégation </p>', unsafe_allow_html=True)

                desagration_list = [" ", "Infrastructures sanitaires","Lieu d'accouchement","Etat vaccinal","Types de vaccination",
                                    "Pathologie","Tranche d'âge","Maladies du PEV","Maladies infectieuses",
                                    "Infections respiratoire aigüe","Maladies IST","Type de Maladie","Activités IEC","Services Médicaux"]

                level_of_disaggregation = st.selectbox(" ", desagration_list, label_visibility='hidden')
            else:
                st.warning(f"Le niveau de desagrégation pour cet indicateur \n{nom_indicateur} n'est pas encore disponible")
        else:
            st.warning("Indicateur non trouvé")





    st.markdown('<p class="custom-label">---------------------------------------------------------------------------------------------------------------------</p>', unsafe_allow_html=True)


    # Options pour les cycles et niveaux
    def create_options(data):
        return {item[1]: item[0] for item in data}

    # Cycle section
    cycle = g_vie.get_cycle()
    cycle_options = create_options(cycle)



    # Charger id et le nom des différents niveaux
    prescolaire_niveau = g_vie.get_niveau_prescolaire()
    prescolaire_options = create_options(prescolaire_niveau)

    primaire = g_vie.get_niveau_primaire()
    primaire_options = create_options(primaire)

    secondaire_pre = g_vie.get_niveau_secondaire_1er_cycle()
    scond_1er_cycle_options = create_options(secondaire_pre)

    secondaire_2eme_cycle=g_vie.get_niveau_secondaire_2nd_cycle()
    secondaire_2eme_cycle_options=create_options(secondaire_2eme_cycle)

    sexes = go.get_sexes()
    sexe_options1 =create_options(sexes)
    sexe_options2 = {'': None, **create_options(sexes)}

    # Formulaire pour l'insertion des données
    if entity_type and entity_name and level_of_disaggregation:
        with st.form("data_entry_form"):
            if level_of_disaggregation == "Cycle":
                valeurs = []
                annees = []
                cycle_ids = []

                # Créer trois colonnes
                col1, col2, col3 = st.columns(3)

                for idx, (cycle, cycle_id) in enumerate(cycle_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{cycle}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{cycle_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    cycle_ids.append(cycle_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer "):
                    for cycle_id, valeur, annee in zip(cycle_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            sexe_id=None,
                            valeur=valeur,
                            annee=annee,
                            cycle_id=cycle_id
                        )
                    st.success("Valeurs enregistrées avec succès.")


            elif level_of_disaggregation == "Niveau préscolaire":
                valeurs = []
                annees = []
                prescolaire_nv_ids = []

                # Créer trois colonnes
                col1, col2, col3 = st.columns(3)

                for idx, (presco, prescol_id) in enumerate(prescolaire_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{presco}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{prescol_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    prescolaire_nv_ids.append(prescol_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer "):
                    for prescol_id, valeur, annee in zip(prescolaire_nv_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            niveau_prescolaire_id=prescol_id
                        )
                    st.success("Valeurs enregistrées avec succès.")


            #Section primaire
            elif level_of_disaggregation == "Niveau primaire":
                valeurs = []
                annees = []
                primaire_nv_ids = []

                # Créer trois colonnes
                col1, col2, col3 = st.columns(3)

                for idx, (prima, prima_id) in enumerate(primaire_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{prima}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{prima_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    primaire_nv_ids.append(prima_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer "):
                    for prima_id, valeur, annee in zip(primaire_nv_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            niveau_primaire_id=prima_id
                        )
                    st.success("Valeurs enregistrées avec succès.")





            # Section Niveau Secondaire 1er cycle
            elif level_of_disaggregation == "Niveau Secondaire 1er cycle":
                valeurs = []
                annees = []
                secondaire_1er_cycle_ids = []

                # Créer trois colonnes
                col1, col2, col3 = st.columns(3)

                for idx, (sec1, sec1_id) in enumerate(scond_1er_cycle_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{sec1}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{sec1_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    secondaire_1er_cycle_ids.append(sec1_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer "):
                    for sec1_id, valeur, annee in zip(secondaire_1er_cycle_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            niveau_secondaire_1er_cycle_id=sec1_id
                        )
                    st.success("Valeurs enregistrées avec succès.")


            # Section Niveau Secondaire 2nd cycle
            elif level_of_disaggregation == "Niveau Secondaire 2nd cycle":
                valeurs = []
                annees = []
                secondaire_2eme_cycle_ids = []

                # Créer trois colonnes
                col1, col2, col3 = st.columns(3)

                for idx, (sec2, sec2_id) in enumerate(secondaire_2eme_cycle_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{sec2}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{sec2_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    secondaire_2eme_cycle_ids.append(sec2_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer "):
                    for sec2_id, valeur, annee in zip(secondaire_2eme_cycle_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            niveau_secondaire_2nd_cycle_id=sec2_id
                        )
                    st.success("Valeurs enregistrées avec succès.")


            # Section Niveau Technique
            elif level_of_disaggregation == "Niveau Technique":
                valeurs = []
                annees = []
                niveau_technique_ids = []

                # Récupération des options pour le Niveau Technique depuis la base de données
                niveau_technique = g_vie.get_niveau_technique()
                niveau_technique_options = create_options(niveau_technique)

                # Créer quatre colonnes
                col1, col2, col3, col4 = st.columns(4)

                for idx, (tech, tech_id) in enumerate(niveau_technique_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 4 == 0:
                        col = col1
                    elif idx % 4 == 1:
                        col = col2
                    elif idx % 4 == 2:
                        col = col3
                    else:
                        col = col4

                    with col:
                        st.markdown(f'<p class="custom-label">{tech}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{tech_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    niveau_technique_ids.append(tech_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer "):
                    for tech_id, valeur, annee in zip(niveau_technique_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            niveau_technique_id=tech_id
                        )
                    st.success("Valeurs enregistrées avec succès.")



            # Section Niveau Supérieur
            elif level_of_disaggregation == "Niveau Supérieur":
                valeurs = []
                annees = []
                niveau_superieur_ids = []

                # Récupération des options pour le Niveau Supérieur depuis la base de données
                niveau_superieur = g_vie.get_niveau_superieur()
                niveau_superieur_options = create_options(niveau_superieur)

                # Créer trois colonnes
                col1, col2, col3 = st.columns(3)

                for idx, (sup, sup_id) in enumerate(niveau_superieur_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{sup}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{sup_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    niveau_superieur_ids.append(sup_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer "):
                    for sup_id, valeur, annee in zip(niveau_superieur_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            niveau_superieur_id=sup_id
                        )
                    st.success("Valeurs enregistrées avec succès.")


            # Section Niveau Professionnel
            elif level_of_disaggregation == "Niveau Professionnel":
                valeurs = []
                annees = []
                niveau_professionnel_ids = []

                # Récupération des options pour le Niveau Professionnel depuis la base de données
                niveau_professionnel = g_vie.get_niveau_professionnel()
                niveau_professionnel_options = create_options(niveau_professionnel)

                # Créer trois colonnes
                col1, col2, col3 = st.columns(3)

                for idx, (pro, pro_id) in enumerate(niveau_professionnel_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{pro}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{pro_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    niveau_professionnel_ids.append(pro_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer"):
                    for pro_id, valeur, annee in zip(niveau_professionnel_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            niveau_professionnel_id=pro_id
                        )
                    st.success("Valeurs enregistrées avec succès.")


            # Section Sexe
            elif level_of_disaggregation == "Sexe":
                valeurs = []
                annees = []
                sexe_ids = []

                # Créer trois colonnes
                col1, col2, col3 = st.columns(3)

                for idx, (sexe, sexe_id) in enumerate(sexe_options1.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{sexe}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{sexe_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    sexe_ids.append(sexe_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer "):
                    for sexe_id, valeur, annee in zip(sexe_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            sexe_id=sexe_id
                        )
                    st.success("Valeurs enregistrées avec succès.")


            # Section Type d'examen
            elif level_of_disaggregation == "Type d'examen":
                valeurs = []
                annees = []
                type_examen_ids = []

                # Récupération des options pour le Type d'examen depuis la base de données
                type_examen = g_vie.get_type_examen()
                type_examen_options = create_options(type_examen)

                # Créer trois colonnes
                col1, col2, col3 = st.columns(3)

                for idx, (exam, exam_id) in enumerate(type_examen_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{exam}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{exam_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    type_examen_ids.append(exam_id)

                # Bouton de soumission
                if st.form_submit_button("Enregistrer "):
                    for exam_id, valeur, annee in zip(type_examen_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            type_examen_id=exam_id
                        )
                    st.success("Valeurs enregistrées avec succès.")





            elif level_of_disaggregation == "Groupe d'âge":
                groupe_age = go.get_groue_age()
                groupe_options = create_options(groupe_age)
                valeurs = []
                annees = []
                groupe_age_ids = []

                # Sélection du sexe en dehors de la boucle, car il est unique pour tous les groupes d'âge
                st.markdown(f'<p class="custom-label">Choisir le sexe</p>', unsafe_allow_html=True)
                selected_sexe = st.selectbox("Choisir le sexe", options=list(sexe_options2.keys()), key=f"value_sexe",
                                             label_visibility='hidden')

                # Créer quatre colonnes
                col1, col2, col3, col4 = st.columns(4)

                for idx, (grpe_age, grpe_age_id) in enumerate(groupe_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 4 == 0:
                        col = col1
                    elif idx % 4 == 1:
                        col = col2
                    elif idx % 4 == 2:
                        col = col3
                    else:
                        col = col4

                    with col:
                        st.markdown(f'<p class="custom-label">{grpe_age} ans</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{grpe_age_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    groupe_age_ids.append(grpe_age_id)

                # Bouton de soumission
                if st.form_submit_button(f"Enregistrer "):
                    for grpe_age_id, valeur, annee in zip(groupe_age_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            sexe_id=selected_sexe,
                            valeur=valeur,
                            annee=annee,
                            groupe_age_id=grpe_age_id
                        )
                    st.success("Valeurs pour Groupe d'âge enregistrées avec succès.")



            #Santé

            elif level_of_disaggregation == "Infrastructures sanitaires":
                infrastructures_sanitaires = g_vie.get_infrastructures_sanitaires()
                infrastructures_sanitaires_options = create_options(infrastructures_sanitaires)
                valeurs = []
                annees = []
                infrastructures_sanitaires_ids = []

                # Créer cinq colonnes
                col1, col2, col3, col4 = st.columns(4)

                for idx, (infra_sanit, infra_sanit_id) in enumerate(infrastructures_sanitaires_options.items()):
                    # Choisir la colonne en fonction de l'index
                    if idx % 4 == 0:
                        col = col1
                    elif idx % 4 == 1:
                        col = col2
                    elif idx % 4 == 2:
                        col = col3

                    else:
                        col = col4

                    with col:
                        st.markdown(f'<p class="custom-label">{infra_sanit}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{infra_sanit_id}",
                                                 label_visibility='hidden')

                    # Ajouter les valeurs dans les listes respectives
                    valeurs.append(valeur)
                    annees.append(annee)
                    infrastructures_sanitaires_ids.append(infra_sanit_id)

                # Bouton de soumission
                if st.form_submit_button(f"Enregistrer "):
                    for infra_sanit_id, valeur, annee in zip(infrastructures_sanitaires_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            infrastructures_sanitaires_id=infra_sanit_id
                        )
                    st.success("Valeurs pour Infrastructures sanitaires enregistrées avec succès.")




            elif level_of_disaggregation == "Lieu d'accouchement":
                lieux_accouchement = g_vie.get_lieu_accouchement()
                lieux_accouchement_options = create_options(lieux_accouchement)
                valeurs = []
                annees = []
                lieux_accouchement_ids = []

                col1, col2, col3= st.columns(3)

                for idx, (lieu_acc, lieu_acc_id) in enumerate(lieux_accouchement_options.items()):
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{lieu_acc}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{lieu_acc_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    lieux_accouchement_ids.append(lieu_acc_id)

                if st.form_submit_button(f"Enregistrer "):
                    for lieu_acc_id, valeur, annee in zip(lieux_accouchement_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            lieu_accouchement_id=lieu_acc_id
                        )
                    st.success("Valeurs pour Lieu d'accouchement enregistrées avec succès.")



            elif level_of_disaggregation == "Etat vaccinal":
                etats_vaccinaux = g_vie.get_etat_vaccinal()
                etats_vaccinaux_options = create_options(etats_vaccinaux)
                valeurs = []
                annees = []
                etats_vaccinaux_ids = []

                col1, col2, col3 = st.columns(3)

                for idx, (etat_vacc, etat_vacc_id) in enumerate(etats_vaccinaux_options.items()):
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{etat_vacc}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{etat_vacc_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    etats_vaccinaux_ids.append(etat_vacc_id)

                if st.form_submit_button(f"Enregistrer "):
                    for etat_vacc_id, valeur, annee in zip(etats_vaccinaux_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            etat_vaccinal_id=etat_vacc_id
                        )
                    st.success("Valeurs pour Etat vaccinal enregistrées avec succès.")



            elif level_of_disaggregation == "Types de vaccination":
                types_vaccination = g_vie.get_types_de_vaccination()
                types_vaccination_options = create_options(types_vaccination)
                valeurs = []
                annees = []
                types_vaccination_ids = []

                col1, col2, col3 = st.columns(3)

                for idx, (type_vacc, type_vacc_id) in enumerate(types_vaccination_options.items()):
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2

                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{type_vacc}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{type_vacc_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    types_vaccination_ids.append(type_vacc_id)

                if st.form_submit_button(f"Enregistrer "):
                    for type_vacc_id, valeur, annee in zip(types_vaccination_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            types_de_vaccination_id=type_vacc_id
                        )
                    st.success("Valeurs pour Types de vaccination enregistrées avec succès.")



            elif level_of_disaggregation == "Pathologie":
                pathologies = g_vie.get_pathologie()
                pathologies_options = create_options(pathologies)
                valeurs = []
                annees = []
                pathologies_ids = []

                col1, col2, col3, col4 = st.columns(4)

                for idx, (patho, patho_id) in enumerate(pathologies_options.items()):
                    if idx % 4 == 0:
                        col = col1
                    elif idx % 4 == 1:
                        col = col2
                    elif idx % 4 == 2:
                        col = col3
                    else:
                        col = col4

                    with col:
                        st.markdown(f'<p class="custom-label">{patho}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{patho_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    pathologies_ids.append(patho_id)

                if st.form_submit_button(f"Enregistrer "):
                    for patho_id, valeur, annee in zip(pathologies_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            pathologie_id=patho_id
                        )
                    st.success("Valeurs pour Pathologie enregistrées avec succès.")




            elif level_of_disaggregation == "Tranche d'âge":
                tranches_age = g_vie.get_tranche_age()
                tranches_age_options = create_options(tranches_age)
                valeurs = []
                annees = []
                tranches_age_ids = []

                col1, col2, col3, col4 = st.columns(4)

                for idx, (tranche_age, tranche_age_id) in enumerate(tranches_age_options.items()):
                    if idx % 4 == 0:
                        col = col1
                    elif idx % 4 == 1:
                        col = col2
                    elif idx % 4 == 2:
                        col = col3

                    else:
                        col = col4

                    with col:
                        st.markdown(f'<p class="custom-label">{tranche_age}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{tranche_age_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    tranches_age_ids.append(tranche_age_id)

                if st.form_submit_button(f"Enregistrer "):
                    for tranche_age_id, valeur, annee in zip(tranches_age_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            tranche_age_id=tranche_age_id
                        )
                    st.success("Valeurs pour Tranche d'âge enregistrées avec succès.")



            elif level_of_disaggregation == "Maladies du PEV":
                maladies_pev = g_vie.get_maladies_du_pev()
                maladies_pev_options = create_options(maladies_pev)
                valeurs = []
                annees = []
                maladies_pev_ids = []

                col1, col2, col3, col4, col5 = st.columns(5)

                for idx, (mal_pev, mal_pev_id) in enumerate(maladies_pev_options.items()):
                    if idx % 5 == 0:
                        col = col1
                    elif idx % 5 == 1:
                        col = col2
                    elif idx % 5 == 2:
                        col = col3
                    elif idx % 5 == 3:
                        col = col4
                    else:
                        col = col5

                    with col:
                        st.markdown(f'<p class="custom-label">{mal_pev}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{mal_pev_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    maladies_pev_ids.append(mal_pev_id)

                if st.form_submit_button(f"Enregistrer"):
                    for mal_pev_id, valeur, annee in zip(maladies_pev_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            maladies_du_pev_id=mal_pev_id
                        )
                    st.success("Valeurs pour Maladies du PEV enregistrées avec succès.")



            elif level_of_disaggregation == "Maladies infectieuses":
                maladies_infectieuses = g_vie.get_maladies_infectieuses()
                maladies_infectieuses_options = create_options(maladies_infectieuses)
                valeurs = []
                annees = []
                maladies_infectieuses_ids = []

                col1, col2, col3, col4 = st.columns(4)

                for idx, (mal_infect, mal_infect_id) in enumerate(maladies_infectieuses_options.items()):
                    if idx % 4 == 0:
                        col = col1
                    elif idx % 4 == 1:
                        col = col2
                    elif idx % 4 == 2:
                        col = col3

                    else:
                        col = col4

                    with col:
                        st.markdown(f'<p class="custom-label">{mal_infect}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{mal_infect_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    maladies_infectieuses_ids.append(mal_infect_id)

                if st.form_submit_button(f"Enregistrer "):
                    for mal_infect_id, valeur, annee in zip(maladies_infectieuses_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            maladies_infectieuses_id=mal_infect_id
                        )
                    st.success("Valeurs pour Maladies infectieuses enregistrées avec succès.")



            elif level_of_disaggregation == "Infections respiratoire aigüe":
                infections_respiratoires_aigues = g_vie.get_infections_respiratoires()
                infections_respiratoires_aigues_options = create_options(infections_respiratoires_aigues)
                valeurs = []
                annees = []
                infections_respiratoires_aigues_ids = []

                col1, col2, col3 = st.columns(3)

                for idx, (inf_resp, inf_resp_id) in enumerate(infections_respiratoires_aigues_options.items()):
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2

                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{inf_resp}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{inf_resp_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    infections_respiratoires_aigues_ids.append(inf_resp_id)

                if st.form_submit_button(f"Enregistrer "):
                    for inf_resp_id, valeur, annee in zip(infections_respiratoires_aigues_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            infection_respiratoire=inf_resp_id
                        )
                    st.success("Valeurs pour Infections respiratoire aigüe enregistrées avec succès.")



            elif level_of_disaggregation == "Maladies IST":
                maladies_ist = g_vie.get_maladies_ist()
                maladies_ist_options = create_options(maladies_ist)
                valeurs = []
                annees = []
                maladies_ist_ids = []

                col1, col2, col3= st.columns(3)

                for idx, (mal_ist, mal_ist_id) in enumerate(maladies_ist_options.items()):
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2

                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{mal_ist}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{mal_ist_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    maladies_ist_ids.append(mal_ist_id)

                if st.form_submit_button(f"Enregistrer "):
                    for mal_ist_id, valeur, annee in zip(maladies_ist_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                           maladies_ist_id=mal_ist_id
                        )
                    st.success("Valeurs pour Maladies IST enregistrées avec succès.")



            elif level_of_disaggregation == "Type de Maladie":
                types_maladie = g_vie.get_type_de_maladie()
                types_maladie_options = create_options(types_maladie)
                valeurs = []
                annees = []
                types_maladie_ids = []

                col1, col2, col3= st.columns(3)

                for idx, (type_mal, type_mal_id) in enumerate(types_maladie_options.items()):
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2

                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{type_mal}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{type_mal_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    types_maladie_ids.append(type_mal_id)

                if st.form_submit_button(f"Enregistrer"):
                    for type_mal_id, valeur, annee in zip(types_maladie_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                           type_de_maladie_id=type_mal_id
                        )
                    st.success("Valeurs pour Type de Maladie enregistrées avec succès.")



            elif level_of_disaggregation == "Activités IEC":
                activites_iec = g_vie.get_activites_iec()
                activites_iec_options = create_options(activites_iec)
                valeurs = []
                annees = []
                activites_iec_ids = []

                col1, col2, col3= st.columns(3)

                for idx, (act_iec, act_iec_id) in enumerate(activites_iec_options.items()):
                    if idx % 3 == 0:
                        col = col1
                    elif idx % 3 == 1:
                        col = col2
                    else:
                        col = col3

                    with col:
                        st.markdown(f'<p class="custom-label">{act_iec}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{act_iec_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    activites_iec_ids.append(act_iec_id)

                if st.form_submit_button(f"Enregistrer "):
                    for act_iec_id, valeur, annee in zip(activites_iec_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            activites_iec_id=act_iec_id
                        )
                    st.success("Valeurs pour Activités IEC enregistrées avec succès.")


            elif level_of_disaggregation == "Services Médicaux":
                services_medicaux = g_vie.get_service_medicaux()
                services_medicaux_options = create_options(services_medicaux)
                valeurs = []
                annees = []
                services_medicaux_ids = []

                col1, col2, col3, col4 = st.columns(4)

                for idx, (service_medic, service_medic_id) in enumerate(services_medicaux_options.items()):
                    if idx % 4 == 0:
                        col = col1
                    elif idx % 4 == 1:
                        col = col2
                    elif idx % 4 == 2:
                        col = col3
                    else:
                        col = col4

                    with col:
                        st.markdown(f'<p class="custom-label">{service_medic}</p>', unsafe_allow_html=True)
                        valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{service_medic_id}",
                                                 label_visibility='hidden')

                    valeurs.append(valeur)
                    annees.append(annee)
                    services_medicaux_ids.append(service_medic_id)

                if st.form_submit_button(f"Enregistrer "):
                    for service_medic_id, valeur, annee in zip(services_medicaux_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur,
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            service_medicaux_id=service_medic_id
                        )
                    st.success("Valeurs pour Services Médicaux enregistrées avec succès.")

    return

dom_condt_vie_menage()
#import affichage_data
#df=affichage_data.afficher_valeurs_indicateurs('annuiare.db')
#st.dataframe(df)
