import streamlit as st


st.title("Página 1")
st.header("Información General")

folio = st.text_input("1. Folio (Consecutivo):")
impacto_proyecto = st.selectbox("2. Impacto en el Proyecto:", ["Alto", "Medio"])
fecha = st.date_input("3. Fecha:")
id_proyecto = st.text_input("4. ID Proyecto:")
nombre_proyecto = st.text_input("5. Proyecto:")
disenador_tecnico = st.text_input("6. Diseñador Técnico:")
nombre_componente = st.text_input("7. Nombre del Componente:")
descripcion_funcional = st.text_area("8. Descripción Funcional:")
requerimientos_tecnicos = st.text_area("9. Requerimientos Técnicos:")

   
