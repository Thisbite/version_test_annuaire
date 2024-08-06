import streamlit as st
import get_object as go

# Streamlit interface
st.title("Formulaire Dynamique pour Valeurs Indicateurs")

indicators = go.get_indicators()
indicator_options = {ind[1]: ind[0] for ind in indicators}
selected_indicator = st.selectbox("Choisir un Indicateur", list(indicator_options.keys()))

level_of_disaggregation = st.selectbox("Niveau de Désagrégation", ["Sexe", "Région", "Département", "Sous-Préfecture", "Groupe d'âge"])

# Region selection with empty option
regions = go.get_regions()
region_options = {reg[1]: reg[0] for reg in regions}

sexes = go.get_sexes()
sexe_options1 = {sex[1]: sex[0] for sex in sexes}
sexe_options1={"":None,**sexe_options1}


region_options = {"": None, **region_options}  # Add empty option
selected_region = st.selectbox("Choisir une Région", list(region_options.keys()))

# Check if a valid region is selected before proceeding
if selected_region and region_options[selected_region]:
    # Département selection based on selected region
    departments = go.get_departments(region_options[selected_region])
    department_options = {dep[1]: dep[0] for dep in departments}
    department_options = {"": None, **department_options}  # Add empty option
    selected_department = st.selectbox("Choisir un Département", list(department_options.keys()))


        # Sous-Préfecture selection based on selected department
    sous_prefectures = go.get_sous_prefectures(department_options[selected_department])
    sous_prefecture_options = {sous_pref[1]: sous_pref[0] for sous_pref in sous_prefectures}
    sous_prefecture_options = {"": None, **sous_prefecture_options}  # Add empty option
    selected_sous_prefecture = st.selectbox("Choisir une Sous-Préfecture", list(sous_prefecture_options.keys()))

        # Handle disaggregation level
    if level_of_disaggregation == "Sexe":
        sexes = go.get_sexes()
        sexe_options = {sex[1]: sex[0] for sex in sexes}
        for sexe, sexe_id in sexe_options.items():
            valeur = st.number_input(f"Valeur pour {sexe}", min_value=0.0, step=0.1, key=f"value_{sexe_id}")
            annee = st.number_input(f"Année pour {sexe}", min_value=2000, max_value=2100, step=1, key=f"year_{sexe_id}")
            if st.button(f"Enregistrer Valeur pour {sexe}", key=f"button_{sexe_id}"):
                go.insert_value(indicator_options[selected_indicator], region_options[selected_region],
                                department_options[selected_department], sous_prefecture_options[selected_sous_prefecture],
                                 sexe_id, valeur, annee,None)
                st.success(f"Valeur pour {sexe} enregistrée avec succès.")

    elif level_of_disaggregation == "Région":
            # Handle région specific data entry
        pass

    elif level_of_disaggregation == "Département":
            # Handle département specific data entry
        pass

    elif level_of_disaggregation == "Sous-Préfecture":
        valeur = st.number_input("Valeur ", min_value=0.0, step=0.1, key="value_sous")
        annee = st.number_input("Année pour ", min_value=2000, max_value=2100, step=1, key="year_sous")
        if st.button("Enregistrer Valeur ", key="button_sous"):
            go.insert_value(indicator_options[selected_indicator], region_options[selected_region],
                             department_options[selected_department], sous_prefecture_options[selected_sous_prefecture],
                             None, valeur, annee,None)
            st.success("Valeur enregistrée avec succès.")

    elif level_of_disaggregation == "Groupe d'âge":
        groupe_age = go.get_groue_age()
        groupe_options = {grpe_age[1]: grpe_age[0] for grpe_age in groupe_age}
        for grpe_age, grpe_age_id in groupe_options.items():
            valeur = st.number_input(f"Valeur pour {grpe_age}", min_value=0.0, step=0.1, key=f"value_{grpe_age_id}")
            annee = st.number_input(f"Année pour {grpe_age}", min_value=2000, max_value=2100, step=1, key=f"year_{grpe_age_id}")
            selected_sexe = st.selectbox("Choisir le sexe", options=list(sexe_options1.keys()),key=f"value{grpe_age_id}")
            if st.button(f"Enregistrer Valeur pour {grpe_age}", key=f"button_{grpe_age_id}"):
                go.insert_value(indicator_options[selected_indicator], region_options[selected_region],
                             department_options[selected_department], sous_prefecture_options[selected_sous_prefecture],
                             sexe_options1[selected_sexe], valeur, annee,grpe_age_id)
                st.success(f"Valeur pour {grpe_age} enregistrée avec succès.")
            # Handle groupe d'âge specific data entry


else:
    st.warning("Veuillez sélectionner une région valide.")