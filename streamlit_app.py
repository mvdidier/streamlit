import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd

# Título de la aplicación
st.title("Asistente de Toma de Decisiones")

# Subtítulo
st.subheader("Comparar opciones: Comprar, Reutilizar o Desarrollar")

# Datos de ejemplo
data = {
    "Criterio": ["Costo", "Tiempo de implementación", "Mantenimiento", "Personalización"],
    "Comprar": [3, 4, 2, 1],
    "Reutilizar": [2, 3, 4, 2],
    "Desarrollar": [4, 2, 3, 5],
}
df = pd.DataFrame(data)

# Configuración de la tabla interactiva
st.write("### Tabla de comparación")
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(enabled=True)  # Activar paginación
gb.configure_default_column(editable=True)  # Permitir edición
gb.configure_selection(selection_mode="single", use_checkbox=True)  # Selección de filas con checkbox
grid_options = gb.build()

# Mostrar la tabla
grid_response = AgGrid(
    df,
    gridOptions=grid_options,
    enable_enterprise_modules=False,
    height=300,
    theme="alpine",  # Temas disponibles: 'streamlit', 'light', 'dark', 'alpine'
)

# Capturar la fila seleccionada
selected_rows = grid_response["selected_rows"]
if selected_rows:
    st.write("### Opción seleccionada")
    st.json(selected_rows)

# Recomendación basada en los datos seleccionados
if selected_rows:
    st.write("### Recomendación:")
    criterio = selected_rows[0]["Criterio"]
    st.write(f"Según el criterio seleccionado: **{criterio}**, podrías considerar la opción con el puntaje más alto.")
else:
    st.write("Selecciona una fila para obtener una recomendación.")
