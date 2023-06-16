import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *
import datetime

if __name__ == "__main__":
    if check_connection():
        st.markdown("## :blue[Istruttori] Disponibili")
        col1, col2 = st.columns(2)
        with col1:
            cognome = st.text_input("Digitare il cognome dell'istruttore", value='')
        with col2:
            input = st.date_input("Selezionare range date", value=(datetime.date(2023, 1, 1), datetime.date(2023, 1, 15)))
        
        query = f"SELECT COUNT(*) FROM istruttore WHERE Cognome = '{cognome}' AND DataNascita > '{input[0]}' AND DataNascita < '{input[1]}'"
        x = execute_query(st.session_state['connection'], query)
        row = x.fetchone()
        if row[0] == 0:
            st.markdown("### :red[Errore] : nessun istruttore corrisponde ai dati selezionati")
        else:
            query = f"SELECT Nome, Cognome, DataNascita, Email FROM istruttore WHERE Cognome = '{cognome}' AND DataNascita > '{input[0]}' AND DataNascita < '{input[1]}'"
            istruttori = execute_query(st.session_state['connection'], query)
            df = pd.DataFrame(istruttori)
            st.table(df)