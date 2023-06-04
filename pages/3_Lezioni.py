import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *
import datetime

if __name__ == "__main__":
    if check_connection():
        st.markdown("## :blue[Lezioni] Programmate")
        st.markdown("### Lezioni per :red[orario]")
        query = "SELECT COUNT(*) AS NumLez, OraInizio FROM programma GROUP BY OraInizio"
        NumLezioni = execute_query(st.session_state['connection'], query)
        df = pd.DataFrame(NumLezioni, columns=['NumLez','OraInizio'])
        chart_data = pd.Series(df['NumLez'].values, index=df['OraInizio'])
        st.bar_chart(chart_data, use_container_width=True)

        st.markdown("### Lezioni per :red[giorno]")
        query = "SELECT COUNT(*) AS Numero, Giorno FROM programma GROUP BY Giorno"
        Dati = execute_query(st.session_state['connection'], query)
        df = pd.DataFrame(Dati, columns=['Numero','Giorno'])
        chart_data = pd.Series(df['Numero'].values, index=df['Giorno'])
        st.line_chart(chart_data, use_container_width=True)