import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *

if __name__ == "__main__":
    if check_connection():
        st.markdown("## :blue[Selezionare] i corsi")
        col1, col2 = st.columns(2)
        with col1:
            option = st.selectbox('Selezionare il tipo di corso', ('Spinning','Attività musicale','Yoga', 'Piscina'))
            num_corsi = execute_query(st.session_state['connection'], f"SELECT COUNT(*) AS num FROM `corsi` WHERE Tipo = '{option}'")
        with col2:
            level = st.slider('Selezionare il livello', 1, 4, 1)
        
        num_corsi = execute_query(st.session_state['connection'], f"SELECT COUNT(*) AS num FROM `corsi` WHERE Tipo = '{option}' AND Livello = '{level}'")
        row = num_corsi.fetchone()
        count = row[0]
        if count == 0:
            st.markdown("# :red[Errore] : nessun risultato trovato")
        else:
            query = f"SELECT Giorno AS 'day', OraInizio AS 'oraI', Durata AS 'dura'  FROM `corsi`, `programma` WHERE Tipo = '{option}' AND Livello = '{level}' AND corsi.CodC = programma.CodC "
            programmi = execute_query(st.session_state['connection'], query)
            with st.expander("Programmi disponibili", expanded=True):
                st.markdown(f"### :blue[Programmi disponibili] di {option} al livello {level}")
                for x in programmi:
                    col1, col2, col3 = st.columns(3)
                    day = x[0]
                    oraI = x[1]
                    dura = x[2]
                    col1.metric('Giorno', day)
                    col2.metric('Ora di Inizio', oraI)
                    col3.metric('Durata (minuti)', dura)
