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
        font-size: 1.5rem;

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
            st.write(f"Entité géographique trouvée : {entity_type}")
            st.write(f"Nom : {entity_name}")
        st.write("---------------------")

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
        st.write("---------------------")
        # Section indicateur
        st.markdown('<p class="custom-label">Entrez le code indicateur</p>', unsafe_allow_html=True)
        ind = st.number_input(" ", min_value=0, step=1,key="ind1",label_visibility='hidden')
        indicator = go.get_indicators(ind)
        st.write("---------------------")

        level_of_disaggregation = None  # Initialize with None

        if indicator:
            id_indicateur, nom_indicateur = indicator
            st.write(f"Indicateur trouvé : {nom_indicateur}")
            st.write(f"Code indicateur entré: {id_indicateur}")

            if 2001 <= id_indicateur <= 2999:
                st.write("---------------------")
                st.markdown('<p class="custom-label">Choisir le niveau désagrégation</p>', unsafe_allow_html=True)

                desagration_list = ["", "Niveau préscolaire", "Cycle", "Niveau primaire", "Niveau Secondaire 1er cycle",
                                    "Niveau Secondaire 2nd cycle", "Niveau Technique", "Niveau Supérieur",
                                    "Niveau Professionnel",
                                    "Sexe", "Type d'examen"]

                level_of_disaggregation = st.selectbox(" ", desagration_list, label_visibility='hidden')
            else:
                st.warning(f"Le niveau de desagrégation pour cet indicateur \n{nom_indicateur} n'est pas encore disponible")
        else:
            st.warning("Indicateur non trouvé")





    st.markdown('<p class="custom-label">----------------------------------------Début --------------------------------------------</p>', unsafe_allow_html=True)


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
    sexe_options1 = {"": None, **create_options(sexes)}




    # Formulaire pour l'insertion des données
    if entity_type and entity_name and level_of_disaggregation:
        with st.form("data_entry_form"):
            if level_of_disaggregation == "Cycle":
                valeurs = []
                annees = []
                cycle_ids = []
                for cycle, cycle_id in cycle_options.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {cycle}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{cycle_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    cycle_ids.append(cycle_id)

                if st.form_submit_button("Enregistrer Valeurs"):
                    for cycle_id, valeur, annee in zip(cycle_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=id_indicateur, region_id=region_id,
                            department_id=department_id, sous_prefecture_id=sous_prefecture_id,
                            sexe_id=None, valeur=valeur, annee=annee, cycle_id=cycle_id
                        )
                    st.success("Valeurs enregistrées avec succès.")

            elif level_of_disaggregation == "Niveau préscolaire":
                valeurs = []
                annees = []
                prescolaire_nv_ids = []

                for presco, prescol_id in prescolaire_options.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {presco}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{prescol_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    prescolaire_nv_ids.append(prescol_id)

                if st.form_submit_button("Enregistrer Valeurs"):
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

                for prima, prima_id in primaire_options.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {prima}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{prima_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    primaire_nv_ids.append(prima_id)

                if st.form_submit_button("Enregistrer Valeurs"):
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
                    st.success(f"Valeurs enregistrées avec succès.")




            # Section Niveau Secondaire 1er cycle
            elif level_of_disaggregation == "Niveau Secondaire 1er cycle":
                valeurs = []
                annees = []
                secondaire_1er_cycle_ids = []

                for sec1, sec1_id in scond_1er_cycle_options.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {sec1}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{sec1_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    secondaire_1er_cycle_ids.append(sec1_id)

                if st.form_submit_button("Enregistrer Valeurs"):
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

                for sec2, sec2_id in secondaire_2eme_cycle_options.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {sec2}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{sec2_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    secondaire_2eme_cycle_ids.append(sec2_id)

                if st.form_submit_button("Enregistrer Valeurs"):
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

                # Ajoutez ici la récupération des options pour le Niveau Technique depuis la base de données
                niveau_technique = g_vie.get_niveau_technique()
                niveau_technique_options = create_options(niveau_technique)

                for tech, tech_id in niveau_technique_options.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {tech}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{tech_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    niveau_technique_ids.append(tech_id)

                if st.form_submit_button("Enregistrer Valeurs"):
                    for tech_id, valeur, annee in zip(niveau_technique_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                                indicator_id=id_indicateur,
                                region_id=region_id,
                                department_id=department_id,
                                sous_prefecture_id=sous_prefecture_id,
                                valeur=valeur,
                                annee=annee,
                                niveau_technique_id=tech_id

                                #niveau_technique_id=tech_id
                            )
                    st.success("Valeurs enregistrées avec succès.")

            # Section Niveau Supérieur
            elif level_of_disaggregation == "Niveau Supérieur":
                valeurs = []
                annees = []
                niveau_superieur_ids = []

                # Ajoutez ici la récupération des options pour le Niveau Supérieur depuis la base de données
                niveau_superieur = g_vie.get_niveau_superieur()
                niveau_superieur_options = create_options(niveau_superieur)

                for sup, sup_id in niveau_superieur_options.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {sup}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{sup_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    niveau_superieur_ids.append(sup_id)

                if st.form_submit_button("Enregistrer Valeurs"):
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

                # Ajoutez ici la récupération des options pour le Niveau Professionnel depuis la base de données
                niveau_professionnel = g_vie.get_niveau_professionnel()
                niveau_professionnel_options = create_options(niveau_professionnel)

                for pro, pro_id in niveau_professionnel_options.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {pro}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{pro_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    niveau_professionnel_ids.append(pro_id)

                if st.form_submit_button("Enregistrer Valeurs"):
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

                for sexe, sexe_id in sexe_options1.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {sexe}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{sexe_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    sexe_ids.append(sexe_id)

                if st.form_submit_button("Enregistrer Valeurs"):
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

                # Ajoutez ici la récupération des options pour le Type d'examen depuis la base de données
                type_examen = g_vie.get_type_examen()
                type_examen_options = create_options(type_examen)

                for exam, exam_id in type_examen_options.items():
                    st.markdown(f'<p class="custom-label">Valeur pour {exam}</p>', unsafe_allow_html=True)
                    valeur = st.number_input(" ", min_value=0, step=1, key=f"value_{exam_id}",label_visibility='hidden')
                    valeurs.append(valeur)
                    annees.append(annee)
                    type_examen_ids.append(exam_id)

                if st.form_submit_button("Enregistrer Valeurs"):
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


    return

dom_condt_vie_menage()
