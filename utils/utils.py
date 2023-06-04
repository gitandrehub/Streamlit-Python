import streamlit as st
from sqlalchemy import create_engine,text

#connettersi all'engine
def connect_db(dialect,username,password,host,dbname):
    try:
        engine=create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}')
        conn=engine.connect()
        return conn
    except:
        return False

def execute_query(conn,query):
    return conn.execute(text(query))

#Controllare se la connessione al db è stata effettuata
def check_connection():
    if "connection" not in st.session_state.keys():
        st.session_state["connection"]=False

    if st.sidebar.button("Connettiti al Database"):
        myconnection=connect_db(dialect="mysql+pymysql",username="root",password="",host="localhost",dbname="palestra")
        if myconnection is not False:
            st.session_state["connection"]=myconnection

        else:
            st.session_state["connection"]=False
            st.sidebar.error("Errore nella connessione al DB")

    if st.session_state["connection"]:
        st.sidebar.success("Connesso al DB")
        return True