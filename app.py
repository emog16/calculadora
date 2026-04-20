import streamlit as st
import math

st.title("Calculadora Web Pro")

# Usamos columnas para los números
col1, col2 = st.columns(2)
with col1:
    n1 = st.number_input("Primer número", value=0.0)
with col2:
    n2 = st.number_input("Segundo número", value=0.0)

# Botones de operación
st.write("### Operaciones")
c1, c2, c3, c4 = st.columns(4)

if c1.button("Sumar"): st.success(f"Resultado: {n1 + n2}")
if c2.button("Restar"): st.success(f"Resultado: {n1 - n2}")
if c3.button("Multiplicar"): st.success(f"Resultado: {n1 * n2}")
if c4.button("Dividir"): 
    if n2 != 0: st.success(f"Resultado: {n1 / n2}")
    else: st.error("No se puede dividir por cero")

st.write("### Especiales")
ce1, ce2, ce3 = st.columns(3)
if ce1.button("Raíz √"): st.success(f"Resultado: {math.sqrt(n1)}")
if ce2.button("x²"): st.success(f"Resultado: {n1**2}")
if ce3.button("Valor de π"): st.info(f"π ≈ {math.pi}")