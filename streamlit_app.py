import streamlit as st
import json
from copy import deepcopy

# Estructura base del JSON (plantilla vacía)
BASE_JSON = {
   "Folio": "",
   "Impacto en el Proyecto": "",
   "Fecha": "",
   "Id de Proyecto": 0,
   "Componentes": [
      {
         "Nombre del Componente": "",
         "Descripción Funcional": "",
         "Diseñador Técnico": "",
         "Requerimientos Técnicos": [
            {"Requerimento": ""},
            {"Requerimento": ""}
         ],
         "Criterios de Decisión": [
            {"Criterio": ""},
            {"Criterio": ""}
         ],
         "Comparativa": {
            "OpcionesDeSolucion": {
               "Crear": {
                  "Descripcion": "",
                  "DocumentacionYReferencias": "",
                  "ViabilidadTecnica": {
                     "Pregunta": "¿El equipo tiene la capacidad técnica para desarrollar el componente?",
                     "Respuesta": ""
                  },
                  "ViabilidadEconomica": {
                     "Pregunta": "Costos por desarrollo propio (Estimación de recursos necesarios) y análisis de retorno de inversión (ROI).",
                     "Respuesta": ""
                  },
                  "ViabilidadOperacional": {
                     "Pregunta": "¿Cómo afecta cada opción a la operación actual del sistema?",
                     "Respuesta": ""
                  },
                  "RiesgosYMitigaciones": {
                     "Pregunta": "Identifique riesgos y sus respectivas mitigaciones.",
                     "Respuesta": ""
                  },
                  "Evaluacion": {
                     "Pregunta": "Puntos fuertes y débiles de cada opción basados en criterios predefinidos.",
                     "Respuesta": ""
                  }
               },
               "Reusar": {
                  "Descripcion": "",
                  "DocumentacionYReferencias": "",
                  "ViabilidadTecnica": {
                     "Pregunta": "¿Los componentes existentes se pueden integrar fácilmente?",
                     "Respuesta": ""
                  },
                  "ViabilidadEconomica": {
                     "Pregunta": "Costos de reusar adaptando (Estimación de recursos necesarios) y análisis de retorno de inversión (ROI).",
                     "Respuesta": ""
                  },
                  "ViabilidadOperacional": {
                     "Pregunta": "¿Cómo afecta cada opción a la operación actual del sistema?",
                     "Respuesta": ""
                  },
                  "RiesgosYMitigaciones": {
                     "Pregunta": "Identifique riesgos y sus respectivas mitigaciones.",
                     "Respuesta": ""
                  },
                  "Evaluacion": {
                     "Pregunta": "Puntos fuertes y débiles de cada opción basados en criterios predefinidos.",
                     "Respuesta": ""
                  }
               },
               "Comprar": {
                  "Descripcion": "",
                  "DocumentacionYReferencias": "",
                  "ViabilidadTecnica": {
                     "Pregunta": "¿Los componentes existentes se pueden integrar fácilmente?",
                     "Respuesta": ""
                  },
                  "ViabilidadEconomica": {
                     "Pregunta": "Costos de compra y tipo de licencia (Estimación de recursos necesarios) y análisis de retorno de inversión (ROI).",
                     "Respuesta": ""
                  },
                  "ViabilidadOperacional": {
                     "Pregunta": "¿Cómo afecta cada opción a la operación actual del sistema?",
                     "Respuesta": ""
                  },
                  "RiesgosYMitigaciones": {
                     "Pregunta": "Identifique riesgos y sus respectivas mitigaciones.",
                     "Respuesta": ""
                  },
                  "Evaluacion": {
                     "Pregunta": "Puntos fuertes y débiles de cada opción basados en criterios predefinidos.",
                     "Respuesta": ""
                  }
               }
            }
         },
         "Alternativa seleccionada": "",
         "Justificación": ""
      }
   ],
   "Firmas": [
      {
         "Nombre": "",
         "Puesto": ""
      }
   ]
}

# Simulación de un "almacén" en memoria (lista de proyectos).
# En un escenario real, podrías guardar/consultar en una BD o servicio externo.
db_proyectos = []

def mostrar_proyectos_en_tabla():
    """
    Función auxiliar para mostrar todos los proyectos cargados
    en una tabla en la interfaz.
    """
    if not db_proyectos:
        st.warning("No hay proyectos registrados.")
        return

    # Para mostrar en tabla, convertimos a un formato plano (o mostrar en JSON).
    for i, proyecto in enumerate(db_proyectos):
        st.write(f"**Proyecto #{i+1}**")
        st.json(proyecto)
        st.write("---")

def formulario_proyecto(proyecto):
    """
    Renderiza el formulario principal para un proyecto dado.
    Retorna un diccionario con los datos actualizados.
    """
    st.subheader("Datos Generales")
    proyecto["Folio"] = st.text_input("Folio", proyecto["Folio"])
    proyecto["Impacto en el Proyecto"] = st.text_input("Impacto en el Proyecto", proyecto["Impacto en el Proyecto"])
    proyecto["Fecha"] = st.text_input("Fecha", proyecto["Fecha"])
    proyecto["Id de Proyecto"] = st.number_input("Id de Proyecto", value=proyecto["Id de Proyecto"], step=1)

    # Por simplicidad, asumimos que solo hay un elemento en "Componentes"
    # Si necesitas múltiples componentes, podrías hacer un bucle similar al de "Firmas".
    componente = proyecto["Componentes"][0]

    st.subheader("Componente")
    componente["Nombre del Componente"] = st.text_input("Nombre del Componente", componente["Nombre del Componente"])
    componente["Descripción Funcional"] = st.text_area("Descripción Funcional", componente["Descripción Funcional"])
    componente["Diseñador Técnico"] = st.text_input("Diseñador Técnico", componente["Diseñador Técnico"])

    # Requerimientos Técnicos
    st.subheader("Requerimientos Técnicos")
    for i, req in enumerate(componente["Requerimientos Técnicos"]):
        req["Requerimento"] = st.text_input(f"Requerimiento #{i+1}", req["Requerimento"])

    # Criterios de Decisión
    st.subheader("Criterios de Decisión")
    for i, criterio in enumerate(componente["Criterios de Decisión"]):
        criterio["Criterio"] = st.text_input(f"Criterio #{i+1}", criterio["Criterio"])

    # Comparativa
    st.subheader("Comparativa de Opciones de Solución")
    opciones_sol = componente["Comparativa"]["OpcionesDeSolucion"]

    for opcion_key, opcion_val in opciones_sol.items():
        st.markdown(f"### {opcion_key.capitalize()}")
        opcion_val["Descripcion"] = st.text_input(f"Descripción ({opcion_key})", opcion_val["Descripcion"])
        opcion_val["DocumentacionYReferencias"] = st.text_area(
            f"Documentacion y Referencias ({opcion_key})",
            opcion_val["DocumentacionYReferencias"]
        )
        with st.expander(f"Viabilidad Técnica ({opcion_key})"):
            st.write(opcion_val["ViabilidadTecnica"]["Pregunta"])
            opcion_val["ViabilidadTecnica"]["Respuesta"] = st.text_area(
                f"Respuesta técnica ({opcion_key})",
                opcion_val["ViabilidadTecnica"]["Respuesta"]
            )
        with st.expander(f"Viabilidad Económica ({opcion_key})"):
            st.write(opcion_val["ViabilidadEconomica"]["Pregunta"])
            opcion_val["ViabilidadEconomica"]["Respuesta"] = st.text_area(
                f"Respuesta económica ({opcion_key})",
                opcion_val["ViabilidadEconomica"]["Respuesta"]
            )
        with st.expander(f"Viabilidad Operacional ({opcion_key})"):
            st.write(opcion_val["ViabilidadOperacional"]["Pregunta"])
            opcion_val["ViabilidadOperacional"]["Respuesta"] = st.text_area(
                f"Respuesta operacional ({opcion_key})",
                opcion_val["ViabilidadOperacional"]["Respuesta"]
            )
        with st.expander(f"Riesgos y Mitigaciones ({opcion_key})"):
            st.write(opcion_val["RiesgosYMitigaciones"]["Pregunta"])
            opcion_val["RiesgosYMitigaciones"]["Respuesta"] = st.text_area(
                f"Respuesta riesgos ({opcion_key})",
                opcion_val["RiesgosYMitigaciones"]["Respuesta"]
            )
        with st.expander(f"Evaluación ({opcion_key})"):
            st.write(opcion_val["Evaluacion"]["Pregunta"])
            opcion_val["Evaluacion"]["Respuesta"] = st.text_area(
                f"Respuesta evaluación ({opcion_key})",
                opcion_val["Evaluacion"]["Respuesta"]
            )

    # Opción seleccionada
    componente["Alternativa seleccionada"] = st.selectbox(
        "Alternativa seleccionada",
        ("Crear", "Reusar", "Comprar"),
        index=["Crear", "Reusar", "Comprar"].index(componente["Alternativa seleccionada"])
        if componente["Alternativa seleccionada"] in ["Crear", "Reusar", "Comprar"] else 0
    )
    componente["Justificación"] = st.text_area("Justificación", componente["Justificación"])

    # Firmas
    st.subheader("Firmas")
    # Suponiendo que hay múltiples firmas, iteramos:
    for i, firma in enumerate(proyecto["Firmas"]):
        firma["Nombre"] = st.text_input(f"Nombre (Firma #{i+1})", firma["Nombre"])
        firma["Puesto"] = st.text_input(f"Puesto (Firma #{i+1})", firma["Puesto"])

    return proyecto

def main():
    st.title("Gestión de Proyectos (CRUD) con Streamlit")

    # Sección para mostrar los proyectos existentes
    st.header("Lista de Proyectos Registrados")
    mostrar_proyectos_en_tabla()

    st.header("Operaciones (Altas, Bajas, Cambios)")

    # Opción para seleccionar la operación
    operacion = st.selectbox("Selecciona una operación", ["Alta", "Cambio", "Baja"])

    if operacion == "Alta":
        st.subheader("Crear un nuevo proyecto")
        # Creamos una copia del JSON base para llenarlo
        nuevo_proyecto = deepcopy(BASE_JSON)
        nuevo_proyecto = formulario_proyecto(nuevo_proyecto)

        if st.button("Guardar nuevo proyecto"):
            # Simulamos guardar en base de datos
            db_proyectos.append(nuevo_proyecto)
            st.success("Proyecto creado exitosamente.")

    elif operacion == "Cambio":
        st.subheader("Modificar un proyecto existente")
        if not db_proyectos:
            st.warning("No hay proyectos para modificar.")
        else:
            # Seleccionar índice de proyecto a modificar
            indices = [f"Proyecto #{i+1}" for i in range(len(db_proyectos))]
            seleccion = st.selectbox("Selecciona proyecto a modificar", indices)
            idx = indices.index(seleccion)

            # Cargar el proyecto en el formulario
            proyecto_seleccionado = db_proyectos[idx]
            proyecto_actualizado = formulario_proyecto(deepcopy(proyecto_seleccionado))

            if st.button("Guardar cambios"):
                db_proyectos[idx] = proyecto_actualizado
                st.success("Proyecto modificado exitosamente.")

    elif operacion == "Baja":
        st.subheader("Eliminar un proyecto")
        if not db_proyectos:
            st.warning("No hay proyectos para eliminar.")
        else:
            indices = [f"Proyecto #{i+1}" for i in range(len(db_proyectos))]
            seleccion = st.selectbox("Selecciona proyecto a eliminar", indices)
            idx = indices.index(seleccion)

            if st.button("Eliminar proyecto"):
                # Simulamos la eliminación
                db_proyectos.pop(idx)
                st.success("Proyecto eliminado exitosamente.")

    st.write("---")
    st.header("Visualización Final de la BD (JSON)")
    st.json(db_proyectos)

if __name__ == "__main__":
    main()
