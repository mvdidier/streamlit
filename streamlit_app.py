import streamlit as st

# Título e Introducción
st.title("Asistente de Toma de Decisiones para Componentes")
st.markdown("""
Bienvenido al asistente de toma de decisiones. Esta herramienta te ayudará a determinar si debes **comprar**, **reutilizar** 
o **desarrollar** un componente basado en tus necesidades y restricciones específicas.
""")

# Paso 1: Definir los Requisitos del Componente
st.header("Paso 1: Definir Requisitos")
funcionalidad = st.text_input("¿Qué funcionalidad necesita el componente?")
complejidad = st.radio("¿Qué tan compleja es la funcionalidad?", ("Baja", "Media", "Alta"))
urgencia = st.radio("¿Qué tan urgente es la necesidad del componente?", ("Baja", "Media", "Alta"))

# Paso 2: Presupuesto y Recursos
st.header("Paso 2: Evaluar Presupuesto y Recursos")
presupuesto = st.number_input("¿Cuál es tu presupuesto para el componente? ($)", min_value=0)
expertise_equipo = st.radio("¿Tu equipo tiene experiencia para desarrollar el componente?", ("Sí", "No"))
tiempo_disponible = st.slider("¿Cuánto tiempo tienes disponible para desarrollar o integrar el componente? (semanas)", 1, 52, 4)

# Paso 3: Explorar Alternativas
st.header("Paso 3: Evaluar Alternativas")
disponibilidad_mercado = st.radio("¿Existe un componente similar disponible en el mercado?", ("Sí", "No"))
reusabilidad = st.radio("¿Puedes reutilizar un componente existente de otro proyecto?", ("Sí", "No"))

# Lógica de Decisión
if st.button("Obtener Recomendación"):
    if complejidad == "Baja" and disponibilidad_mercado == "Sí":
        st.success("Recomendación: Compra un componente preconstruido para ahorrar tiempo y esfuerzo.")
    elif reusabilidad == "Sí" and expertise_equipo == "Sí":
        st.success("Recomendación: Reutiliza un componente existente de tus proyectos.")
    elif complejidad == "Alta" and expertise_equipo == "No" and presupuesto > 5000:
        st.success("Recomendación: Considera contratar a un tercero para desarrollar el componente.")
    else:
        st.warning("Recomendación: Desarrolla el componente internamente si tu equipo tiene experiencia y suficiente tiempo.")

# Notas Opcionales
st.header("Notas Adicionales")
st.text_area("Agrega aquí cualquier nota o consideración adicional.")
