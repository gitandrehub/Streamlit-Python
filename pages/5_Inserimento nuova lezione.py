import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *

if __name__ == "__main__":
    if check_connection():
        st.markdown("## :blue[Inserimento] nuova lezione settimanale")
        with st.form("form"):
            st.subheader("Inserire i dati richiesti")
            # istruttore
            query = "SELECT CodFisc  FROM `istruttore`"
            lista = execute_query(st.session_state['connection'], query)
            values = lista.fetchall()
            istruttori = [f"{value[0]}" for value in values]
            istruttore = st.selectbox('Codice fiscale del istruttore:', istruttori)
            # codice corso
            query = "SELECT CodC FROM `corsi`"
            lista = execute_query(st.session_state['connection'], query)
            values = lista.fetchall()
            codici = [f"{value[0]}" for value in values]
            codice = st.selectbox('Codice del corso:', codici)
            # giorno
            giorno = st.selectbox('Giorno:', ('Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì'))
            # ora inizio
            ora = st.slider('Ora:', 0, 23, 12)
            minuti = st.slider('Minuti:', 0, 60, 30)
            oraInizio = f"{ora}:{minuti}:00"
            # durata della lezione
            durata = st.slider('Durata della lezione:', 1, 60, 30)
            # sala
            sala = st.text_input('Sala')
            submitted = st.form_submit_button("Inserisci nuova lezione")

        if submitted:
            query = f"SELECT COUNT(*) FROM `programma` WHERE CodC = '{codice}' AND Giorno = '{giorno}'"
            values = execute_query(st.session_state['connection'], query)
            count = values.fetchone()[0]
            if(count == 0):
                st.markdown("### Nuova lezione inserita")
                query = f"INSERT INTO `programma`(CodFisc, Giorno, OraInizio, Durata, Sala, CodC) VALUES('{istruttore}', '{giorno}', '{oraInizio}', '{durata}', '{sala}', '{codice}')"
                execute_query(st.session_state['connection'], query)
            else:
                st.markdown("### Errore: lezione già presente in quel giorno")
