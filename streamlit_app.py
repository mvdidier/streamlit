import streamlit as st

# Título e Introducción
st.title("Asistente de Toma de Decisiones para Componentes")
st.markdown("""
Bienvenido al asistente de toma de decisiones. Esta herramienta te ayudará a determinar si debes **comprar**, **reutilizar** 
o **desarrollar** un componente basado en tus necesidades y restricciones específicas.
""")

# Paso 1: Definir los Requisitos del Componente
st.header("Paso 1: Definir Requisitos")
nombre = st.text_input("¿Cual es el nombre del componente?")
proyecto = st.text_input("¿Cual es el nombre del proyecto?")
impacto = st.radio("¿Cual es el impacto en el proyecto?", ("Baja", "Media", "Alta"))

descripcionfuncional = st.text_input("Proporciona una descripcion funcional de este componente")
requerimientotecnicos = st.text_input("Proporciona los requerimientos técnicos")

disenadortecnico = st.text_input("¿Cual es el nombre del diseñador técnico?")


# Lógica de Decisión
#if st.button("Obtener Recomendación"):
#    if complejidad == "Baja" and disponibilidad_mercado == "Sí":
#        st.success("Recomendación: Compra un componente preconstruido para ahorrar tiempo y esfuerzo.")
#    elif reusabilidad == "Sí" and expertise_equipo == "Sí":
#        st.success("Recomendación: Reutiliza un componente existente de tus proyectos.")
#    elif complejidad == "Alta" and expertise_equipo == "No" and presupuesto > 5000:
#        st.success("Recomendación: Considera contratar a un tercero para desarrollar el componente.")
#    else:
#        st.warning("Recomendación: Desarrolla el componente internamente si tu equipo tiene experiencia y suficiente tiempo.")

# Notas Opcionales
st.header("Notas Adicionales")
st.text_area("Agrega aquí cualquier nota o consideración adicional.")
