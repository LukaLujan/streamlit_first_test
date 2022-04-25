import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")

st.title("Aplikacija za izdavanje kredita")
st.write("""
# Izaberite parametre sa lijeve strane

 """)


columns =['Spol', 'Brak', 'Djeca', 'Faks', 'Samozaposlen',
       'Mjeseci',"Kreditna Povijest" ,"Tip Naselja", "Mjesečni_Prihod", "Prihod_Jamca","Mjesečna Rata"]


def user_input_features():
    spol=st.sidebar.selectbox("Izaberite Spol", ("M", "Ž"))
    brak =st.sidebar.selectbox("Izaberite Bračni Status", ("Da", "Ne"))
    djeca =st.sidebar.selectbox("Izaberite broj djece", ("0", "1", "2","3"))
    faks =st.sidebar.selectbox("Završen fakultet", ("Da", "Ne"))
    zap = st.sidebar.selectbox("Samozaposlen", ("Da", "Ne"))
    mjeseci =st.sidebar.slider("Izaberite broj mjeseci", 12,480,12,6)
    povijest =st.sidebar.selectbox("Izaberite kredintu prošlost 0 je negativna, 1 je pozitivna ili kada netko prvi put ide po kredit", ("0", "1"))
    naselje = st.sidebar.selectbox("Izaberi vrstu naselja", ("Grad","Predgrad", "Selo"))
    zprihod =st.sidebar.number_input("Upišite mjesečni prihod zajmoprimca", min_value=0 )
    jprihod =st.sidebar.number_input("Upišite mjesečni prihod jamca ili ostavi 0 ako ne postoji jamac", min_value=0 )
    kredit =st.sidebar.number_input("Upišite traženu mjesečnu ratu", min_value=0 )


    informacije =[spol, brak, djeca, faks, zap, mjeseci,povijest, naselje, zprihod, jprihod, kredit]
    dataframe_predic = pd.DataFrame([informacije], columns=columns)
    return dataframe_predic

inputs = user_input_features()




import pickle
filename = 'finalized_modell.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

prediction=loaded_model.predict(inputs)
prediction_proba = loaded_model.predict_proba(inputs)[0][1]

# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

st.subheader("User Input Parameters")
st.write(inputs)

st.subheader("Potencijalna klasifikacija zajmoprimca")
if prediction =="Pozitivan":
    st.write("Dobar")
else:
    st.write("Loš")


st.subheader("Stataistička vjerojatnost da je zajmoprimac 'pozitivan' ")
st.write(round(prediction_proba,2))