import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *

if __name__ == "__main__":
    st.set_page_config(
        page_title="La mia App",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://dbdmg.polito.it/',
            'Report a bug': "https://dbdmg.polito.it/",
            'About': "# Corso di *Basi di Dati*"
        }
    )
    st.markdown("# :black[Sviluppo di un’applicazione web con Streamlit e MySQL 📕]")
    st.markdown(" ### :red[Introduzione]")
    st.markdown("Ho sviluppato l'applicazione richiesta principalmente usando markdown per scrivere titoli, sottotitoli e messaggi; Per gli input invece sono stati utilizzati dei form (nelle due pagine conclusive), select box, slider e qualche box in cui l'utente deve scrivere.")
    st.markdown(" ### :red[Obiettivo]")
    st.markdown("Creare un’applicazione web in Python (Streamlit) in grado di interagire con un database MySQL in modo da eseguire interrogazioni in base alle interazioni dell’utente. ")
    st.markdown(" ### :blue[Studente]")
    st.markdown("Andrea Cauda, Matricola 300505")
    
    if "connection" not in st.session_state.keys():
        st.session_state["connection"] = False

    check_connection()


