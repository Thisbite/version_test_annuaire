import streamlit as st
import get_object as go
import get_domaine_condt_vie_menage as g_vie

def dom_condt_vie_menage():
    # CSS for styling the form
    st.markdown("""
        <style>
            .stForm {
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 20px;
                background-color: #87CEEB; /* Sky blue background color */
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .stForm h2 {
                color: #4CAF50;
            }
            .stForm .stButton>button {
                background-color: #4CAF50;
                color: white;
            }
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
        </style>
    """, unsafe_allow_html=True)

    st.title("Formulaire de collecte")

    # Entrée du code d'entité géographique
    with st.expander("Entrée de code d'entité géographique"):
        code_entite = st.number_input("Saisie le code de l'entité géographique ", min_value=0, step=1)

        entity_type, entity_name = go.get_geographical_entity_name(code_entite)
        if entity_type and entity_name:
            st.write(f"Entité géographique trouvée : {entity_type}")
            st.write(f"Nom : {entity_name}")

        region_id = None
        department_id = None
        sous_prefecture_id = None

        # Pour recupérer le code entité géographique
        region = go.get_region_name(code_entite) if code_entite else None
        department = go.get_department_name(code_entite) if code_entite else None
        sous_prefecture = go.get_sous_prefecture_name(code_entite) if code_entite else None

        if region:
            region_id = code_entite

        if department:
            department_id = code_entite

        if sous_prefecture:
            sous_prefecture_id = code_entite

    # Sélection du code domaine
    with st.expander("Code domaine"):
        ind = st.number_input("Entrez le code du domaine")
        indicators = go.get_indicators(ind)
        indicator_options = {ind[1]: ind[0] for ind in indicators}

    """
    Dans cette section nous récuperons toutes id et nom des variables dans les différentes tables
    """

    # Options pour les cycles et niveaux
    def create_options(data):
        return {item[1]: item[0] for item in data}

    # Cycle section
    cycle = g_vie.get_cycle()
    cycle_options = create_options(cycle)

    # Section préscolaire
    prescolaire_niveau = g_vie.get_niveau_prescolaire()
    prescolaire_options = create_options(prescolaire_niveau)
    prescolaire = g_vie.get_niveau_prescolaire()

    primaire = g_vie.get_niveau_primaire()
    primaire_options = create_options(primaire)

    secondaire_pre = g_vie.get_niveau_secondaire_1er_cycle()
    secondaire_pre_options = create_options(secondaire_pre)

    sexes = go.get_sexes()
    sexe_options1 = {"": None, **create_options(sexes)}



    # Sélection des indicateurs
    with st.expander("Liste indicateurs"):
        selected_indicator = st.selectbox("Choisir un Indicateur", list(indicator_options.keys()))

    st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

    # Niveau de désagrégation
    with st.expander("Niveau désagrégation"):
        level_of_disaggregation = st.selectbox("Choisir le niveau", ["Niveau préscolaire", "Cycle"])

        st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

        annee = st.number_input("Saisie l'année", min_value=2000, max_value=2100, step=1, key="year_g")

    # Formulaire pour l'insertion des données
    if entity_type and entity_name and selected_indicator:
        with st.form("data_entry_form"):
            if level_of_disaggregation == "Cycle":
                valeurs = []
                annees = []
                cycle_ids = []
                for cycle, cycle_id in cycle_options.items():
                    valeur = st.number_input(f"Valeur pour {cycle}", min_value=0.0, step=0.1, key=f"value_{cycle_id}")
                    valeurs.append(valeur)
                    annees.append(annee)
                    cycle_ids.append(cycle_id)

                if st.form_submit_button("Enregistrer Valeurs"):
                    for cycle_id, valeur, annee in zip(cycle_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=indicator_options[selected_indicator], region_id=region_id,
                            department_id=department_id, sous_prefecture_id=sous_prefecture_id,
                             valeur=valeur, annee=annee, cycle_id=cycle_id
                        )
                    st.success("Valeurs enregistrées avec succès.")

            elif level_of_disaggregation == "Niveau préscolaire":
                valeurs = []
                annees = []
                prescolaire_nv_ids = []

                for presco, prescol_id in prescolaire_options.items():
                    valeur = st.number_input(f"Valeur pour {presco}", min_value=0.0, step=0.1,
                                             key=f"value_{prescol_id}")
                    valeurs.append(valeur)
                    annees.append(annee)
                    prescolaire_nv_ids.append(prescol_id)

                if st.form_submit_button("Enregistrer Valeurs"):
                    for prescol_id, valeur, annee in zip(prescolaire_nv_ids, valeurs, annees):
                        g_vie.insert_value_cdt_vie(
                            indicator_id=indicator_options[selected_indicator],
                            region_id=region_id,
                            department_id=department_id,
                            sous_prefecture_id=sous_prefecture_id,
                            valeur=valeur,
                            annee=annee,
                            niveau_prescolaire_id=prescol_id,


                        )
                    st.success("Valeurs enregistrées avec succès.")

    return

dom_condt_vie_menage()

import affichage_data as af
st.write("La base de données possible")
df = af.afficher_valeurs_indicateurs('annuiare.db')
if st.checkbox("Afficher la vue des données"):
    st.dataframe(df)






