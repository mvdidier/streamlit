import streamlit as st
import pandas as pd
import datetime
import uuid

# Función para inicializar datos en sesión
if "data" not in st.session_state:
    st.session_state["data"] = []

if "criteria" not in st.session_state:
    st.session_state["criteria"] = []

if "signatures" not in st.session_state:
    st.session_state["signatures"] = []

# Función para agregar registro
def add_record():
    record = {
        "Folio": str(uuid.uuid4())[:8],
        "Impacto en el Proyecto": impacto,
        "Fecha": fecha,
        "ID Proyecto": id_proyecto,
        "Proyecto": proyecto,
        "Diseñador Técnico": tecnico,
        "Nombre del Componente": componente,
        "Descripción Funcional": descripcion,
        "Requerimientos Técnicos": req_tec.split(","),
        "Criterios de Decisión": criteria.split(","),
        "Alternativa Seleccionada": alternativa,
        "Justificación": justificacion,
        "Firmas de Conformidad": [tuple(firma.split(",")) for firma in firmas.split("\n") if firma]
    }
    st.session_state["data"].append(record)

# Función para editar registro
def edit_record(index):
    st.session_state["data"][index] = {
        "Folio": st.session_state["data"][index]["Folio"],
        "Impacto en el Proyecto": impacto,
        "Fecha": fecha,
        "ID Proyecto": id_proyecto,
        "Proyecto": proyecto,
        "Diseñador Técnico": tecnico,
        "Nombre del Componente": componente,
        "Descripción Funcional": descripcion,
        "Requerimientos Técnicos": req_tec.split(","),
        "Criterios de Decisión": criteria.split(","),
        "Alternativa Seleccionada": alternativa,
        "Justificación": justificacion,
        "Firmas de Conformidad": [tuple(firma.split(",")) for firma in firmas.split("\n") if firma]
    }

# Función para eliminar registro
def delete_record(index):
    st.session_state["data"].pop(index)

# Encabezado de la aplicación
st.title("Gestión de Proyectos")

# Formulario de entrada
with st.form("Formulario de Proyecto"):
    impacto = st.selectbox("Impacto en el Proyecto", ["Alto", "Medio", "Bajo"], key="impacto")
    fecha = st.date_input("Fecha", datetime.date.today(), key="fecha")
    id_proyecto = st.text_input("ID Proyecto", key="id_proyecto")
    proyecto = st.text_input("Proyecto", key="proyecto")
    tecnico = st.text_input("Diseñador Técnico", key="tecnico")
    componente = st.text_input("Nombre del Componente", key="componente")
    descripcion = st.text_area("Descripción Funcional", key="descripcion")

    # Tabla dinámica de Requerimientos Técnicos
    st.subheader("Requerimientos Técnicos")
    req_tec = st.text_area("Ingrese los requerimientos separados por coma", key="req_tec")

    # Criterios de Decisión
    st.subheader("Criterios de Decisión")
    criteria = st.text_area("Ingrese los criterios separados por coma", key="criteria")

    alternativa = st.text_input("Alternativa seleccionada", key="alternativa")
    justificacion = st.text_area("Justificación", key="justificacion")

    # Firmas de Conformidad
    st.subheader("Firmas de Conformidad")
    firmas = st.text_area("Ingrese los firmantes en formato 'Nombre,Puesto' separados por línea", key="firmas")

    submit = st.form_submit_button("Guardar Registro")

if submit:
    add_record()
    st.success("Registro guardado exitosamente")

# Mostrar tabla de registros
st.subheader("Registros Guardados")
if st.session_state["data"]:
    for i, record in enumerate(st.session_state["data"]):
        st.write(f"**Folio**: {record['Folio']}")
        st.write(f"**Impacto en el Proyecto**: {record['Impacto en el Proyecto']}")
        st.write(f"**Fecha**: {record['Fecha']}")
        st.write(f"**ID Proyecto**: {record['ID Proyecto']}")
        st.write(f"**Proyecto**: {record['Proyecto']}")
        st.write(f"**Diseñador Técnico**: {record['Diseñador Técnico']}")
        st.write(f"**Nombre del Componente**: {record['Nombre del Componente']}")
        st.write(f"**Descripción Funcional**: {record['Descripción Funcional']}")
        st.write(f"**Requerimientos Técnicos**: {', '.join(record['Requerimientos Técnicos'])}")
        st.write(f"**Criterios de Decisión**: {', '.join(record['Criterios de Decisión'])}")
        st.write(f"**Alternativa Seleccionada**: {record['Alternativa Seleccionada']}")
        st.write(f"**Justificación**: {record['Justificación']}")
        st.write("**Firmas de Conformidad**:")
        for firma in record['Firmas de Conformidad']:
            st.write(f"Nombre: {firma[0]}, Puesto: {firma[1]}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Editar", key=f"edit_{i}"):
                with st.form(f"Editar_{i}"):
                    impacto = st.selectbox("Impacto en el Proyecto", ["Alto", "Medio", "Bajo"], index=["Alto", "Medio", "Bajo"].index(record['Impacto en el Proyecto']), key=f"impacto_{i}")
                    fecha = st.date_input("Fecha", record['Fecha'], key=f"fecha_{i}")
                    id_proyecto = st.text_input("ID Proyecto", record['ID Proyecto'], key=f"id_proyecto_{i}")
                    proyecto = st.text_input("Proyecto", record['Proyecto'], key=f"proyecto_{i}")
                    tecnico = st.text_input("Diseñador Técnico", record['Diseñador Técnico'], key=f"tecnico_{i}")
                    componente = st.text_input("Nombre del Componente", record['Nombre del Componente'], key=f"componente_{i}")
                    descripcion = st.text_area("Descripción Funcional", record['Descripción Funcional'], key=f"descripcion_{i}")
                    req_tec = st.text_area("Requerimientos Técnicos", ",".join(record['Requerimientos Técnicos']), key=f"req_tec_{i}")
                    criteria = st.text_area("Criterios de Decisión", ",".join(record['Criterios de Decisión']), key=f"criteria_{i}")
                    alternativa = st.text_input("Alternativa seleccionada", record['Alternativa Seleccionada'], key=f"alternativa_{i}")
                    justificacion = st.text_area("Justificación", record['Justificación'], key=f"justificacion_{i}")
                    firmas = st.text_area("Firmas de Conformidad", "\n".join([f"{firma[0]},{firma[1]}" for firma in record['Firmas de Conformidad']]), key=f"firmas_{i}")
                    save = st.form_submit_button("Guardar Cambios")
                    if save:
                        edit_record(i)
                        st.success("Registro actualizado exitosamente")
        with col2:
            if st.button("Eliminar", key=f"delete_{i}"):
                delete_record(i)
                st.success("Registro eliminado exitosamente")
