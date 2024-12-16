import streamlit as st

# Inicializar variables de control en sesión
if 'page' not in st.session_state:
    st.session_state['page'] = 1

# Funciones de navegación
def change_page(page_number):
    st.session_state['page'] = page_number

# Redirección en la misma ejecución
current_page = st.session_state['page']

# Página 1
if current_page == 1:
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

    if st.button("Siguiente →"):
        change_page(2)

# Página 2
elif current_page == 2:
    st.title("Página 2")
    st.header("Criterios de Selección de Decisiones")

    col1, col2 = st.columns(2)

    with col1:
        st.radio("¿Es necesario personalizar el componente?", ["Sí", "No"], key="p1")
        st.radio("¿Forma parte del núcleo del negocio?", ["Sí", "No"], key="p2")
        st.radio("¿Tiene experiencia previa en desarrollo similar?", ["Sí", "No"], key="p3")
        st.radio("¿Se dispone del tiempo necesario?", ["Sí", "No"], key="p4")
        st.radio("¿Es viable desarrollar dentro del presupuesto?", ["Sí", "No"], key="p5")

    with col2:
        st.radio("¿Existen componentes internos probados?", ["Sí", "No"], key="q1")
        st.radio("¿Se pueden adaptar componentes existentes?", ["Sí", "No"], key="q2")
        st.radio("¿Cumple con los estándares de desarrollo?", ["Sí", "No"], key="q3")
        st.radio("¿Está disponible la documentación técnica?", ["Sí", "No"], key="q4")
        st.radio("¿Se reducirá el tiempo de desarrollo?", ["Sí", "No"], key="q5")

    col_prev, col_next = st.columns(2)
    with col_prev:
        if st.button("← Anterior"):
            change_page(1)
    with col_next:
        st.button("Mostrar Resumen")

