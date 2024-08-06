import form_get as go
import streamlit as st
st.header("Formulaire pour ajouter un domaine")
with st.form("domaine_form"):
    domaine_id = st.number_input("ID du Domaine", min_value=1, step=1)
    nom_domaine = st.text_input("Nom du Domaine")
    if st.form_submit_button("Enregistrer Domaine"):
        go.insert_domaine(domaine_id, nom_domaine)
        st.success("Domaine enregistré avec succès.")

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

st.header("Formulaire pour ajouter un sous-domaine")
with st.form("sous_domaine_form"):
    sous_domaine_id = st.number_input("ID du Sous-Domaine", min_value=1, step=1)
    f_domaine_id = st.number_input("ID du Domaine Parent", min_value=1, step=1)
    nom_sous_domaine = st.text_input("Nom du Sous-Domaine")
    if st.form_submit_button("Enregistrer Sous-Domaine"):
        go.insert_sous_domaine(sous_domaine_id, f_domaine_id, nom_sous_domaine)
        st.success("Sous-Domaine enregistré avec succès.")

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

st.header("Formulaire pour ajouter un indicateur")
with st.form("indicateur_form"):
    indicateur_id = st.number_input("ID de l'Indicateur", min_value=1, step=1)
    f_sous_domaine_id = st.number_input("ID du Sous-Domaine Parent", min_value=1, step=1)
    nom_indicateur = st.text_input("Nom de l'Indicateur")
    if st.form_submit_button("Enregistrer Indicateur"):
        go.insert_indicateur(indicateur_id, f_sous_domaine_id, nom_indicateur)
        st.success("Indicateur enregistré avec succès.")

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

st.header("Formulaire pour ajouter un sexe")
with st.form("sexe_form"):
    sexe_id = st.number_input("ID du Sexe", min_value=1, step=1)
    sexe = st.text_input("Sexe")
    if st.form_submit_button("Enregistrer Sexe"):
        go.insert_sexe(sexe_id, sexe)
        st.success("Sexe enregistré avec succès.")

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

st.header("Formulaire pour ajouter un groupe d'âge")
with st.form("groupe_age_form"):
    grp_age_id = st.number_input("ID du Groupe d'Âge", min_value=1, step=1)
    groupe_age = st.text_input("Groupe d'Âge")
    if st.form_submit_button("Enregistrer Groupe d'Âge"):
        go.insert_groupe_age(grp_age_id, groupe_age)
        st.success("Groupe d'Âge enregistré avec succès.")

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

st.header("Formulaire pour ajouter un âge")
with st.form("age_form"):
    age_id = st.number_input("ID de l'Âge", min_value=1, step=1)
    age = st.text_input("Âge")
    if st.form_submit_button("Enregistrer Âge"):
        go.insert_age(age_id, age)
        st.success("Âge enregistré avec succès.")

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

st.header("Formulaire pour ajouter une direction statistique")
with st.form("direction_statistique_form"):
    direction_id = st.number_input("ID de la Direction Statistique", min_value=1, step=1)
    description = st.text_input("Description")
    if st.form_submit_button("Enregistrer Direction Statistique"):
        go.insert_direction_statistique(direction_id, description)
        st.success("Direction Statistique enregistrée avec succès.")

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

st.header("Formulaire pour ajouter un directeur")
with st.form("directeur_form"):
    directeur_id = st.number_input("ID du Directeur", min_value=1, step=1)
    nom = st.text_input("Nom du Directeur")
    prenom = st.text_input("Prénom du Directeur")
    email = st.text_input("Email du Directeur")
    numero = st.text_input("Numéro du Directeur")
    if st.form_submit_button("Enregistrer Directeur"):
        go.insert_directeur(directeur_id, nom, prenom, email, numero)
        st.success("Directeur enregistré avec succès.")

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)

st.header("Formulaire pour ajouter un agent de collecte")
with st.form("agent_collecte_form"):
    agent_id = st.number_input("ID de l'Agent de Collecte", min_value=1, step=1)
    nom = st.text_input("Nom de l'Agent de Collecte")
    prenom = st.text_input("Prénom de l'Agent de Collecte")
    email = st.text_input("Email de l'Agent de Collecte")
    numero = st.text_input("Numéro de l'Agent de Collecte")
    if st.form_submit_button("Enregistrer Agent de Collecte"):
        go.insert_agent_collecte(agent_id, nom, prenom, email, numero)
        st.success("Agent de Collecte enregistré avec succès.")
