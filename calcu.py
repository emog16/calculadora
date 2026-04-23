import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="Calculadora Móvil", page_icon="📱")

# --- ESTILO CSS PARA ASPECTO DE TELÉFONO ---
st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        height: 60px;
        border-radius: 50px;
        font-size: 20px;
        font-weight: bold;
        margin: 5px 0px;
    }
    /* Estilo para el área del resultado */
    .result-screen {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 15px;
        text-align: right;
        font-size: 40px;
        color: white;
        margin-bottom: 20px;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("Calculadora Web Pro")

    # Inicializar el estado para los números si no existen
    if 'resultado' not in st.session_state:
        st.session_state.resultado = "0"

    # Pantalla de visualización (como la de un móvil)
    st.markdown(f'<div class="result-screen">{st.session_state.resultado}</div>', unsafe_allow_html=True)

    # Entradas de números
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        n1 = st.number_input("Primer número", value=0.0, format="%.2f")
    with col_n2:
        n2 = st.number_input("Segundo número", value=0.0, format="%.2f")

    st.write("### Operaciones")
    
    # Fila 1: Operaciones Básicas
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("Sumar"):
            st.session_state.resultado = str(n1 + n2)
            st.rerun()
    with c2:
        if st.button("Restar"):
            st.session_state.resultado = str(n1 - n2)
            st.rerun()
    with c3:
        if st.button("Multiplicar"):
            st.session_state.resultado = str(n1 * n2)
            st.rerun()
    with c4:
        if st.button("Dividir"):
            if n2 != 0:
                st.session_state.resultado = str(n1 / n2)
            else:
                st.session_state.resultado = "Error"
            st.rerun()

    st.write("### Especiales")
    
    # Fila 2: Funciones Especiales
    ce1, ce2, ce3, ce4 = st.columns(4)
    with ce1:
        if st.button("Raíz √"):
            if n1 >= 0:
                st.session_state.resultado = str(round(math.sqrt(n1), 4))
            else:
                st.session_state.resultado = "Error"
            st.rerun()
    with ce2:
        if st.button("x²"):
            st.session_state.resultado = str(n1 ** 2)
            st.rerun()
    with ce3:
        if st.button("π"):
            st.session_state.resultado = str(round(math.pi, 4))
            st.rerun()
    with ce4:
        if st.button("AC", help="Limpiar"):
            st.session_state.resultado = "0"
            st.rerun()

if __name__ == "__main__":
    main()
