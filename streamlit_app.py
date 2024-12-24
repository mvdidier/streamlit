import streamlit as st
import sqlite3
from st_aggrid import AgGrid, GridOptionsBuilder
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

# Función para insertar un registro
def insertar_componente(nombre, proyecto, impacto, descripcion_funcional, requerimientos_tecnicos, disenador_tecnico):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''INSERT INTO componentes (
            nombre, proyecto, impacto, descripcion_funcional, requerimientos_tecnicos, disenador_tecnico
        ) VALUES (?, ?, ?, ?, ?, ?)''', (nombre, proyecto, impacto, descripcion_funcional, requerimientos_tecnicos, disenador_tecnico))

# Inicialización de la base de datos
init_db()

# Inicialización del estado
if "seccion" not in st.session_state:
    st.session_state.seccion = 1
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "proyecto" not in st.session_state:
    st.session_state.proyecto = ""
if "impacto" not in st.session_state:
    st.session_state.impacto = "Baja"
if "descripcion_funcional" not in st.session_state:
    st.session_state.descripcion_funcional = ""
if "requerimientos_tecnicos" not in st.session_state:
    st.session_state.requerimientos_tecnicos = ""
if "disenador_tecnico" not in st.session_state:
    st.session_state.disenador_tecnico = ""

# Datos iniciales para la sección 3
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

    st.session_state.nombre = st.text_input("¿Cuál es el nombre del componente?", value=st.session_state.nombre)
    st.session_state.proyecto = st.text_input("¿Cuál es el nombre del proyecto?", value=st.session_state.proyecto)
    st.session_state.impacto = st.radio("¿Cuál es el impacto en el proyecto?", ("Baja", "Media", "Alta"), index=["Baja", "Media", "Alta"].index(st.session_state.impacto))

    if st.button("Ir a Sección 2"):
        if st.session_state.nombre and st.session_state.proyecto:
            st.session_state.seccion = 2
        else:
            st.error("Por favor, completa todos los campos de la Sección 1.")

elif st.session_state.seccion == 2:
    st.header("Sección 2: Detalles Técnicos")

    st.session_state.descripcion_funcional = st.text_input("Proporciona una descripción funcional de este componente", value=st.session_state.descripcion_funcional)
    st.session_state.requerimientos_tecnicos = st.text_input("Proporciona los requerimientos técnicos", value=st.session_state.requerimientos_tecnicos)
    st.session_state.disenador_tecnico = st.text_input("¿Cuál es el nombre del diseñador técnico?", value=st.session_state.disenador_tecnico)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Regresar a Sección 1"):
            st.session_state.seccion = 1

    with col2:
        if st.button("Ir a Sección 3"):
            if st.session_state.descripcion_funcional and st.session_state.requerimientos_tecnicos and st.session_state.disenador_tecnico:
                st.session_state.seccion = 3
            else:
                st.error("Por favor, completa todos los campos de la Sección 2.")

elif st.session_state.seccion == 3:
    st.header("Sección 3: Evaluación de Opciones")

    st.markdown("""
    En esta sección puedes evaluar las opciones de solución para determinar la mejor estrategia basada en criterios técnicos, económicos, operacionales y de riesgos.
    """)

    # Configuración del grid editable
    gb = GridOptionsBuilder.from_dataframe(st.session_state.grid_data)
    gb.configure_default_column(editable=True, resizable=True)
    gb.configure_grid_options(domLayout='autoHeight')
    grid_options = gb.build()

    # Mostrar el grid editable
    response = AgGrid(st.session_state.grid_data, gridOptions=grid_options, editable=True, fit_columns_on_grid_load=True, height=300)

    # Actualizar los datos editados en el estado
    st.session_state.grid_data = pd.DataFrame(response['data'])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Regresar a Sección 2"):
            st.session_state.seccion = 2

    with col2:
        if st.button("Guardar Evaluación"):
            st.success("Evaluación guardada correctamente.")
            st.write("Datos actualizados:")
            st.write(st.session_state.grid_data)
