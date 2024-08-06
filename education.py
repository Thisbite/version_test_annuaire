import streamlit as st
import  sqlite3

#Connexion à la base de donnée
def get_db_connection():
    conn = sqlite3.connect('data_entry.db')
    return conn
#Fonction de listining des indicateurs de la population et ses formulaires
def education():
    conn = get_db_connection()
    c = conn.cursor()

    return
