import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *
import datetime

if __name__ == "__main__":
    if check_connection():
        st.markdown("## :blue[Inserimento] nuovi corsi")
        codC, nome, tipo = " ", " ", " "
        with st.form("form"):
            st.subheader("Inserire i dati richiesti")

            codC = st.text_input("Codice del corso:")
            nome = st.text_input("Nome del corso:")
            tipo = st.text_input("Tipo di corso:")
            livello = st.slider('Livello del corso:',1,4,1)
            submitted = st.form_submit_button("Inserisci")
            
        if submitted:
            query = f"SELECT COUNT(*) FROM corsi WHERE CodC = '{codC}'"
            count = execute_query(st.session_state['connection'], query)
            value = count.fetchone()[0]
            if codC != " " and nome != " " and tipo != " " and value == 0:
                st.success("Dati inseriti in maniera corretta")
                query = f"INSERT INTO `corsi` (CodC, Nome, Tipo, Livello) VALUES('{codC}', '{nome}', '{tipo}', '{livello}')"
                execute_query(st.session_state['connection'], query)
            else:
                st.markdown("### Errore nell'inserimento dei dati (chiave duplicata o dati mancanti)")