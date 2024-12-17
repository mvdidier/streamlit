import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Criterios de Selección", layout="wide")

# Título principal
st.title("Paso 1")
st.subheader("Responda las siguientes preguntas para poder identificar posibles criterios de selección de decisiones")

# Preguntas en listas
col1_questions = [
    "¿Es necesario personalizar el componente para cumplir con requisitos únicos?",
    "¿El componente forma parte del núcleo del negocio o brinda ventaja competitiva?",
    "¿El equipo tiene experiencia previa en desarrollar un componente similar?",
    "¿Se dispone del tiempo necesario para completar el desarrollo?",
    "¿Es viable desarrollar dentro del presupuesto disponible?",
    "¿Se requieren características que no están disponibles en soluciones existentes?",
    "¿El desarrollo propio permitirá un mejor control sobre futuras modificaciones?",
    "¿El componente puede ser reutilizado en otros proyectos futuros?",
    "¿La creación del componente reducirá costos a largo plazo?",
    "¿Los riesgos técnicos son manejables con las capacidades internas del equipo?"
]

col2_questions = [
    "¿Existen componentes internos probados que puedan cumplir con los requisitos?",
    "¿Los componentes existentes pueden ser adaptados con un esfuerzo razonable?",
    "¿El componente reutilizable cumple con los estándares de desarrollo?",
    "¿Está disponible la documentación técnica necesaria para integrarlo?",
    "¿El uso del componente reducirá significativamente los tiempos de desarrollo?",
    "¿Los costos de mantenimiento y soporte son aceptables?",
    "¿Es compatible con las tecnologías actuales del proyecto?",
    "¿El componente ha sido probado en un entorno similar al proyecto actual?",
    "¿La calidad del componente es suficiente para el propósito requerido?",
    "¿El reuso de este componente implica dependencia de un tercero o equipo interno?"
]

col3_questions = [
    "¿Existe en el mercado una solución que cumpla completamente con los requisitos?",
    "¿El proveedor ofrece garantías de soporte técnico y mantenimiento?",
    "¿El costo de adquisición es menor al costo de desarrollo o adaptación interna?",
    "¿La implementación de la solución comprada es rápida y sencilla?",
    "¿El proveedor tiene una buena reputación y referencias en proyectos similares?",
    "¿El producto cumple con estándares de seguridad, privacidad y calidad?",
    "¿El componente comprado se puede integrar sin problemas con los sistemas actuales?",
    "¿El proveedor ofrece actualizaciones regulares para el componente?",
    "¿La licencia o suscripción es viable dentro del presupuesto?",
    "¿El contrato con el proveedor protege los intereses de la organización (propiedad intelectual, penalizaciones)?"
]

# Diseño con tres columnas
col1, col2, col3 = st.columns(3)

# Columna 1
with col1:
    st.write("### Desarrollo Interno")
    for question in col1_questions:
        st.selectbox(question, ["Sí", "No"], key=f"col1_{question}")

# Columna 2
with col2:
    st.write("### Reuso de Componentes")
    for question in col2_questions:
        st.selectbox(question, ["Sí", "No"], key=f"col2_{question}")

# Columna 3
with col3:
    st.write("### Soluciones Externas")
    for question in col3_questions:
        st.selectbox(question, ["Sí", "No"], key=f"col3_{question}")

# Botón final
if st.button("Enviar Respuestas"):
    st.success("Respuestas enviadas exitosamente. ¡Gracias!")
