import streamlit as st
import sqlite3

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

# Función para obtener todos los registros
def obtener_componentes():
    with sqlite3.connect(DB_FILE) as conn:
        return conn.execute('SELECT * FROM componentes').fetchall()

# Función para actualizar un registro
def actualizar_componente(id, nombre, proyecto, impacto, descripcion_funcional, requerimientos_tecnicos, disenador_tecnico):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''UPDATE componentes SET
            nombre = ?,
            proyecto = ?,
            impacto = ?,
            descripcion_funcional = ?,
            requerimientos_tecnicos = ?,
            disenador_tecnico = ?
        WHERE id = ?''', (nombre, proyecto, impacto, descripcion_funcional, requerimientos_tecnicos, disenador_tecnico, id))

# Función para eliminar un registro
def eliminar_componente(id):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('DELETE FROM componentes WHERE id = ?', (id,))

# Inicialización de la base de datos
init_db()

# Título e Introducción
st.title("Asistente de Toma de Decisiones para Componentes")
st.markdown("""
Bienvenido al asistente de toma de decisiones. Esta herramienta te ayudará a determinar si debes **comprar**, **reutilizar** 
o **desarrollar** un componente basado en tus necesidades y restricciones específicas.
""")

# Menú de opciones
opcion = st.sidebar.selectbox("Acción", ["Registrar Componente", "Ver Componentes"])

if opcion == "Registrar Componente":
    # Formulario de registro
    st.header("Registrar Componente")

    nombre = st.text_input("¿Cuál es el nombre del componente?")
    proyecto = st.text_input("¿Cuál es el nombre del proyecto?")
    impacto = st.radio("¿Cuál es el impacto en el proyecto?", ("Baja", "Media", "Alta"))
    descripcion_funcional = st.text_input("Proporciona una descripción funcional de este componente")
    requerimientos_tecnicos = st.text_input("Proporciona los requerimientos técnicos")
    disenador_tecnico = st.text_input("¿Cuál es el nombre del diseñador técnico?")

    if st.button("Guardar Componente"):
        if nombre and proyecto and descripcion_funcional and requerimientos_tecnicos and disenador_tecnico:
            insertar_componente(nombre, proyecto, impacto, descripcion_funcional, requerimientos_tecnicos, disenador_tecnico)
            st.success("Componente registrado exitosamente.")
        else:
            st.error("Por favor, completa todos los campos.")

elif opcion == "Ver Componentes":
    # Mostrar y gestionar componentes
    st.header("Lista de Componentes")
    componentes = obtener_componentes()

    if componentes:
        for componente in componentes:
            with st.expander(f"{componente[1]} - {componente[2]} (ID: {componente[0]})"):
                st.text(f"Impacto: {componente[3]}")
                st.text(f"Descripción Funcional: {componente[4]}")
                st.text(f"Requerimientos Técnicos: {componente[5]}")
                st.text(f"Diseñador Técnico: {componente[6]}")

                if st.button("Editar", key=f"edit-{componente[0]}"):
                    nuevo_nombre = st.text_input("Nuevo nombre", componente[1])
                    nuevo_proyecto = st.text_input("Nuevo proyecto", componente[2])
                    nuevo_impacto = st.radio("Nuevo impacto", ("Baja", "Media", "Alta"), index=["Baja", "Media", "Alta"].index(componente[3]))
                    nueva_descripcion_funcional = st.text_input("Nueva descripción funcional", componente[4])
                    nuevos_requerimientos_tecnicos = st.text_input("Nuevos requerimientos técnicos", componente[5])
                    nuevo_disenador_tecnico = st.text_input("Nuevo diseñador técnico", componente[6])

                    if st.button("Guardar Cambios", key=f"save-{componente[0]}"):
                        actualizar_componente(componente[0], nuevo_nombre, nuevo_proyecto, nuevo_impacto, nueva_descripcion_funcional, nuevos_requerimientos_tecnicos, nuevo_disenador_tecnico)
                        st.success("Componente actualizado exitosamente.")

                if st.button("Eliminar", key=f"delete-{componente[0]}"):
                    eliminar_componente(componente[0])
                    st.success("Componente eliminado exitosamente.")
    else:
        st.warning("No hay componentes registrados.")
