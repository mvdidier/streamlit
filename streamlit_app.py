import streamlit as st
import pandas as pd
import datetime
import uuid

# Inicializar los datos en la sesión
if "data" not in st.session_state:
    st.session_state["data"] = []

if "req_tec_temp" not in st.session_state:
    st.session_state["req_tec_temp"] = []

# Función para agregar registro
def add_record():
    record = {
        "Folio": str(uuid.uuid4())[:8],
        "Impacto en el Proyecto": impacto,
        "Fecha": fecha.strftime("%d/%m/%Y"),
        "ID Proyecto": id_proyecto,
        "Proyecto": proyecto,
        "Diseñador Técnico": tecnico,
        "Nombre del Componente": componente,
        "Descripción Funcional": descripcion,
        "Requerimientos Técnicos": st.session_state["req_tec_temp"],
        "Criterios de Decisión": criterios.split(";"),
        "Alternativa Seleccionada": alternativa,
        "Justificación": justificacion,
        "Firmas de Conformidad": [tuple(firma.split(",")) for firma in firmas.split("\n") if firma]
    }
    st.session_state["data"].append(record)
    st.session_state["req_tec_temp"] = []

# Función para editar registro
def edit_record(index):
    st.session_state["data"][index] = {
        "Folio": st.session_state["data"][index]["Folio"],
        "Impacto en el Proyecto": impacto,
        "Fecha": fecha.strftime("%d/%m/%Y"),
        "ID Proyecto": id_proyecto,
        "Proyecto": proyecto,
        "Diseñador Técnico": tecnico,
        "Nombre del Componente": componente,
        "Descripción Funcional": descripcion,
        "Requerimientos Técnicos": st.session_state["req_tec_temp"],
        "Criterios de Decisión": criterios.split(";"),
        "Alternativa Seleccionada": alternativa,
        "Justificación": justificacion,
        "Firmas de Conformidad": [tuple(firma.split(",")) for firma in firmas.split("\n") if firma]
    }

# Función para eliminar registro
def delete_record(index):
    st.session_state["data"].pop(index)

# Función para gestionar la lista dinámica de Requerimientos Técnicos
def manage_requirements():
    st.subheader("Requerimientos Técnicos")
    new_req = st.text_input("Nuevo Requerimiento Técnico", key="new_req")
    if st.button("Agregar Requerimiento"):
        if new_req:
            st.session_state["req_tec_temp"].append(new_req)
            st.success("Requerimiento agregado.")
        else:
            st.warning("El campo no puede estar vacío.")

    for i, req in enumerate(st.session_state["req_tec_temp"]):
        col1, col2, col3 = st.columns([6, 1, 1])
        with col1:
            st.text(req)
        with col2:
            if st.button("Editar", key=f"edit_req_{i}"):
                st.session_state["req_tec_temp"][i] = st.text_input("Editar Requerimiento", req, key=f"edit_input_{i}")
                st.success("Requerimiento actualizado.")
        with col3:
            if st.button("Eliminar", key=f"delete_req_{i}"):
                st.session_state["req_tec_temp"].pop(i)
                st.success("Requerimiento eliminado.")
                break

# Encabezado
st.title("Gestión de Proyectos")

# Formulario para ingresar datos
with st.form("form_proyecto"):
    impacto = st.selectbox("Impacto en el Proyecto", ["Alto", "Medio", "Bajo"], key="impacto")
    fecha = st.date_input("Fecha", datetime.date.today(), key="fecha")
    id_proyecto = st.text_input("ID Proyecto", key="id_proyecto")
    proyecto = st.text_input("Proyecto", key="proyecto")
    tecnico = st.text_input("Diseñador Técnico", key="tecnico")
    componente = st.text_input("Nombre del Componente", key="componente")
    descripcion = st.text_area("Descripción Funcional", key="descripcion")

    # Manejo de la lista dinámica de Requerimientos Técnicos
    manage_requirements()

    criterios = st.text_area("Criterios de Decisión (separados por punto y coma)", key="criterios")
    alternativa = st.text_input("Alternativa Seleccionada", key="alternativa")
    justificacion = st.text_area("Justificación", key="justificacion")

    firmas = st.text_area("Firmas de Conformidad (Nombre,Puesto separados por línea)", key="firmas")

    guardar = st.form_submit_button("Guardar Registro")

if guardar:
    add_record()
    st.success("Registro guardado exitosamente.")

# Mostrar registros existentes
st.subheader("Registros Guardados")
if st.session_state["data"]:
    for i, record in enumerate(st.session_state["data"]):
        with st.expander(f"Folio: {record['Folio']} - Proyecto: {record['Proyecto']}"):
            st.write(f"**Impacto:** {record['Impacto en el Proyecto']}")
            st.write(f"**Fecha:** {record['Fecha']}")
            st.write(f"**ID Proyecto:** {record['ID Proyecto']}")
            st.write(f"**Diseñador Técnico:** {record['Diseñador Técnico']}")
            st.write(f"**Nombre del Componente:** {record['Nombre del Componente']}")
            st.write(f"**Descripción Funcional:** {record['Descripción Funcional']}")
            st.write("**Requerimientos Técnicos:**")
            for req in record['Requerimientos Técnicos']:
                st.write(f"- {req}")
            st.write(f"**Criterios de Decisión:** {', '.join(record['Criterios de Decisión'])}")
            st.write(f"**Alternativa Seleccionada:** {record['Alternativa Seleccionada']}")
            st.write(f"**Justificación:** {record['Justificación']}")
            st.write("**Firmas de Conformidad:**")
            for firma in record['Firmas de Conformidad']:
                st.write(f"- Nombre: {firma[0]}, Puesto: {firma[1]}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Editar", key=f"edit_{i}"):
                    with st.form(f"edit_form_{i}"):
                        impacto = st.selectbox("Impacto en el Proyecto", ["Alto", "Medio", "Bajo"], index=["Alto", "Medio", "Bajo"].index(record['Impacto en el Proyecto']))
                        fecha = st.date_input("Fecha", datetime.datetime.strptime(record['Fecha'], "%d/%m/%Y").date())
                        id_proyecto = st.text_input("ID Proyecto", record['ID Proyecto'])
                        proyecto = st.text_input("Proyecto", record['Proyecto'])
                        tecnico = st.text_input("Diseñador Técnico", record['Diseñador Técnico'])
                        componente = st.text_input("Nombre del Componente", record['Nombre del Componente'])
                        descripcion = st.text_area("Descripción Funcional", record['Descripción Funcional'])

                        req_tec = st.session_state["req_tec_temp"] = record['Requerimientos Técnicos']

                        criterios = st.text_area("Criterios de Decisión (separados por punto y coma)", ";".join(record['Criterios de Decisión']))
                        alternativa = st.text_input("Alternativa Seleccionada", record['Alternativa Seleccionada'])
                        justificacion = st.text_area("Justificación", record['Justificación'])
                        firmas = st.text_area("Firmas de Conformidad (Nombre,Puesto separados por línea)", "\n".join([f"{firma[0]},{firma[1]}" for firma in record['Firmas de Conformidad']]))
                        guardar_cambios = st.form_submit_button("Guardar Cambios")
                        if guardar_cambios:
                            edit_record(i)
                            st.success("Registro actualizado correctamente.")
            with col2:
                if st.button("Eliminar", key=f"delete_{i}"):
                    delete_record(i)
                    st.success("Registro eliminado correctamente.")
else:
    st.info("No hay registros guardados.")
