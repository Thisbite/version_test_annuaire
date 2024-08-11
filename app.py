import streamlit as st
import get_object as go
import get_domaine_condt_vie_menage as g_vie

st.set_page_config(page_title="Formulaire de collecte", page_icon="📊")
# Injecter le CSS Bootstrap et le style personnalisé
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
       
        .form-divider {
            margin: 20px 0;
            border-bottom: 1px solid #ddd;
        }
        .expander-wrapper {
            border: 2px solid blue;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 20px; /* Space between expanders */
        }
        .custom-bold-text {
            font-weight: bold;
            color: black;
            font-size: 45px; 
        }
      
        .stTextInput label{
            color:blue;
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
        code_entite = st.number_input(" ", min_value=0, step=1,label_visibility='hidden')

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

        if indicator:
            id_indicateur, nom_indicateur = indicator
            st.write(f"Indicateur trouvé : {nom_indicateur}")
            st.write(f"Code indicateur entré:{id_indicateur}")
        else:
            st.warning("Indicateur non trouvé")
            return
        st.write("---------------------")
        st.markdown('<p class="custom-label">Choisir le niveau désagrégation</p>', unsafe_allow_html=True)
        level_of_disaggregation = st.selectbox(" ", ["","Niveau préscolaire", "Cycle","Primaire"],label_visibility='hidden')
    st.markdown('<p class="custom-label">----------------------------------------Début --------------------------------------------</p>', unsafe_allow_html=True)


    # Options pour les cycles et niveaux
    def create_options(data):
        return {item[1]: item[0] for item in data}

    # Cycle section
    cycle = g_vie.get_cycle()
    cycle_options = create_options(cycle)

    # Section préscolaire
    prescolaire_niveau = g_vie.get_niveau_prescolaire()
    prescolaire_options = create_options(prescolaire_niveau)

    primaire = g_vie.get_niveau_primaire()
    primaire_options = create_options(primaire)

    secondaire_pre = g_vie.get_niveau_secondaire_1er_cycle()
    secondaire_pre_options = create_options(secondaire_pre)

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
            elif level_of_disaggregation == "Primaire":

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


    return

dom_condt_vie_menage()
