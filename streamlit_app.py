import streamlit as st
import sqlite3
import pandas as pd

# Configuración de la base de datos
DB_FILE = "componentes.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS componentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            proyecto TEXT,
            impacto TEXT,
            descripcion_funcional TEXT,
            requerimientos_tecnicos TEXT,
            disenador_tecnico TEXT
        )''')

# Inicialización de la base de datos
init_db()

# Inicialización del estado
if "seccion" not in st.session_state:
    st.session_state.seccion = 1
if "grid_data" not in st.session_state:
    st.session_state.grid_data = pd.DataFrame({
        "Opciones de Solución": ["Crear", "Reusar", "Comprar"],
        "Descripción": ["Cómo se crearía el componente.", 
                        "Opciones de componentes existentes que se podrían adaptar.", 
                        "Opciones de componentes disponibles comercialmente."],
        "Viabilidad Técnica": ["¿El equipo tiene la capacidad técnica para desarrollarlo?", 
                               "¿Los componentes existentes se pueden integrar fácilmente?", 
                               "¿Los componentes existentes se pueden integrar fácilmente?"],
        "Viabilidad Económica": ["Costos por desarrollo propio (ROI).", 
                                 "Costos de reusar adaptando (ROI).", 
                                 "Costos de compra y tipo de licencia (ROI)."],
        "Viabilidad Operacional": ["Impacto en la operación actual del sistema.", 
                                   "Impacto en la operación actual del sistema.", 
                                   "Impacto en la operación actual del sistema."],
        "Riesgos y Mitigaciones": ["Análisis de riesgos y mitigaciones.", 
                                   "Análisis de riesgos y mitigaciones.", 
                                   "Análisis de riesgos y mitigaciones."]
    })

# Título e Introducción
st.title("Asistente de Toma de Decisiones para Componentes")
st.markdown("""
Bienvenido al asistente de toma de decisiones. Esta herramienta te ayudará a determinar si debes **comprar**, **reutilizar** 
o **desarrollar** un componente basado en tus necesidades y restricciones específicas.
""")

# Control de secciones
if st.session_state.seccion == 1:
    st.header("Sección 1: Información General")

    nombre = st.text_input("¿Cuál es el nombre del componente?")
    proyecto = st.text_input("¿Cuál es el nombre del proyecto?")
    impacto = st.radio("¿Cuál es el impacto en el proyecto?", ("Baja", "Media", "Alta"))

    if st.button("Ir a Sección 2"):
        if nombre and proyecto:
            st.session_state.seccion = 2
        else:
            st.error("Por favor, completa todos los campos de la Sección 1.")

elif st.session_state.seccion == 2:
    st.header("Sección 2: Detalles Técnicos")

    descripcion_funcional = st.text_input("Proporciona una descripción funcional de este componente")
    requerimientos_tecnicos = st.text_input("Proporciona los requerimientos técnicos")
    disenador_tecnico = st.text_input("¿Cuál es el nombre del diseñador técnico?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Regresar a Sección 1"):
            st.session_state.seccion = 1

    with col2:
        if st.button("Ir a Sección 3"):
            if descripcion_funcional and requerimientos_tecnicos and disenador_tecnico:
                st.session_state.seccion = 3
            else:
                st.error("Por favor, completa todos los campos de la Sección 2.")

elif st.session_state.seccion == 3:
    st.header("Sección 3: Evaluación de Opciones")

    st.markdown("""
    En esta sección puedes evaluar las opciones de solución para determinar la mejor estrategia basada en criterios técnicos, económicos, operacionales y de riesgos.
    """)

    # Mostrar los datos como una tabla editable
    st.write("Tabla Editable")
    edited_df = st.experimental_data_editor(st.session_state.grid_data, num_rows="dynamic")

    # Guardar los cambios
    if st.button("Guardar Evaluación"):
        st.session_state.grid_data = edited_df
        st.success("Evaluación guardada correctamente.")
        st.write("Datos actualizados:")
        st.write(st.session_state.grid_data)
