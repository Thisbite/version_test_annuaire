import streamlit as st
import get_object as go

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

with st.expander("Entrée de code d'entité géographique"):
    code_entite = st.number_input("Saisie le code de l'entité géographique ", min_value=0, step=1)

    entity_type, entity_name = go.get_geographical_entity_name(code_entite)

    if entity_type and entity_name:
        st.write(f"Entité géographie trouvée  : {entity_type}")
        st.write(f"Nom: {entity_name}")

    region_id = None
    department_id = None
    sous_prefecture_id = None

    # Nouveau code et test
    region = go.get_region_name(code_entite) if code_entite else None
    department = go.get_department_name(code_entite) if code_entite else None
    sous_prefecture = go.get_sous_prefecture_name(code_entite) if code_entite else None

    if region:
        region_id = code_entite

    if department:
        department_id = code_entite

    if sous_prefecture:
        sous_prefecture_id = code_entite


with st.expander("Code domaine"):
    ind = st.number_input("Entrez le code du domaine")
indicators = go.get_indicators(ind)
indicator_options = {ind[1]: ind[0] for ind in indicators}
sexes = go.get_sexes()
sexe_options1 = {sex[1]: sex[0] for sex in sexes}
sexe_options1 = {"": None, **sexe_options1}

with st.expander("Liste indicateurs"):
    selected_indicator = st.selectbox("Choisir un Indicateur", list(indicator_options.keys()))

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)
with st.expander("Niveau désagrégation"):
    level_of_disaggregation = st.selectbox("choisir le niveau", ["Sexe", "Groupe d'âge"])

    st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

    annee = st.number_input(f"Saisie l'année ", min_value=2000, max_value=2100, step=1, key=f"year_g")

if entity_type and entity_name and selected_indicator:
    with st.form("data_entry_form"):
        if level_of_disaggregation == "Sexe":
            sexe_options = {sex[1]: sex[0] for sex in sexes}
            valeurs = []
            annees = []
            sexe_ids = []
            for sexe, sexe_id in sexe_options.items():
                valeur = st.number_input(f"Valeur pour {sexe}", min_value=0.0, step=0.1, key=f"value_{sexe_id}")
                valeurs.append(valeur)
                annees.append(annee)
                sexe_ids.append(sexe_id)

            if st.form_submit_button(f"Enregistrer Valeurs"):
                for sexe_id, valeur, annee in zip(sexe_ids, valeurs, annees):
                    print(f"Inserting: {indicator_options[selected_indicator]}, {region_id}, {department_id}, {sous_prefecture_id}, {sexe_id}, {valeur}, {annee}, None")
                    go.insert_value(
                        indicator_options[selected_indicator], region_id,
                        department_id, sous_prefecture_id,
                        sexe_id, valeur, annee, None
                    )
                st.success("Valeurs enregistrées avec succès.")

        elif level_of_disaggregation == "Groupe d'âge":
            groupe_age = go.get_groue_age()
            groupe_options = {grpe_age[1]: grpe_age[0] for grpe_age in groupe_age}
            valeurs = []
            annees = []
            groupe_age_ids = []
            sexe_ids = []
            for grpe_age, grpe_age_id in groupe_options.items():
                valeur = st.number_input(f"Valeur pour {grpe_age}", min_value=0.0, step=0.1, key=f"value_{grpe_age_id}")
                selected_sexe = st.selectbox("Choisir le sexe", options=list(sexe_options1.keys()), key=f"value{grpe_age_id}")
                valeurs.append(valeur)
                annees.append(annee)
                groupe_age_ids.append(grpe_age_id)
                sexe_ids.append(sexe_options1[selected_sexe])

            if st.form_submit_button(f"Enregistrer Valeurs pour Groupe d'âge"):
                for grpe_age_id, valeur, annee, sexe_id in zip(groupe_age_ids, valeurs, annees, sexe_ids):
                    print(f"Inserting: {indicator_options[selected_indicator]}, {region_id}, {department_id}, {sous_prefecture_id}, {sexe_id}, {valeur}, {annee}, {grpe_age_id}")
                    go.insert_value(
                        indicator_options[selected_indicator], region_id,
                        department_id, sous_prefecture_id,
                        sexe_id, valeur, annee, grpe_age_id
                    )
                st.success("Valeurs pour Groupe d'âge enregistrées avec succès.")
else:
    st.warning("Aucune entité géographique trouvée pour le code saisi ou absence d'indicateur")
