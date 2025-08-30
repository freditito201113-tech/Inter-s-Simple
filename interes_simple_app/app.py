import streamlit as st

st.set_page_config(page_title="Calculadora de Interés Simple", page_icon="💰")

st.title("💰 Calculadora de Interés Simple")

st.write("Ingrese los datos para calcular el interés simple:")

# Entradas del usuario
capital = st.number_input("Capital inicial (C):", min_value=0.0, step=100.0)
tasa = st.number_input("Tasa de interés (%) (r):", min_value=0.0, step=0.1)
tiempo = st.number_input("Tiempo (t en años):", min_value=0.0, step=1.0)

# Botón de cálculo
if st.button("Calcular"):
    interes = (capital * tasa * tiempo) / 100
    total = capital + interes

    st.success(f"📊 Interés generado: {interes:.2f}")
    st.info(f"💵 Total acumulado: {total:.2f}")
