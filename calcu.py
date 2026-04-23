import streamlit as st
import math

# Configuración del título
st.title("Calculadora Científica Básica")

# Entrada de número principal
numero = st.number_input("Introduce un número:", value=0.0)

# Columnas para organizar los botones
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Raíz Cuadrada"):
        if numero >= 0:
            resultado = math.sqrt(numero)
            st.success(f"√{numero} = {resultado}")
        else:
            st.error("No se puede calcular la raíz de un número negativo.")

with col2:
    if st.button("Elevado al ²"):
        resultado = math.pow(numero, 2)
        st.success(f"{numero}² = {resultado}")

with col3:
    if st.button("Usar Pi (π)"):
        st.info(f"El valor de π es aproximadamente: {math.pi}")

with col4:
    if st.button("Multiplicar por π"):
        resultado = numero * math.pi
        st.success(f"{numero} * π = {resultado}")

# Sección de ayuda técnica
st.sidebar.markdown("""
### Funciones utilizadas:
* **math.sqrt(x)**: Calcula la raíz cuadrada.
* **math.pow(x, 2)**: Eleva el número a la potencia deseada.
* **math.pi**: Constante matemática universal.
""")