import streamlit as st
import sqlite3

def create_table():
    conn = sqlite3.connect('survey.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS survey (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        phone TEXT,
                        age TEXT,
                        gender TEXT,
                        education TEXT,
                        occupation TEXT,
                        household_size INTEGER,
                        speaks_indigenous_language TEXT,
                        language TEXT,
                        agriculture_main_income TEXT,
                        income_percentage TEXT,
                        crops TEXT,
                        crop_area TEXT,
                        production_volume TEXT,
                        production_value TEXT,
                        waste_percentage TEXT,
                        has_fruit_trees TEXT,
                        fruit_trees TEXT,
                        consume_fruits TEXT,
                        consume_method TEXT,
                        unused_fruits TEXT,
                        tree_age TEXT,
                        planted_trees TEXT,
                        other_fruits_consumed TEXT,
                        other_fruits_source TEXT,
                        childhood_fruits TEXT,
                        childhood_fruit_sources TEXT,
                        consume_childhood_fruits TEXT,
                        reasons_not_consuming TEXT,
                        reasons_fruits_not_known TEXT,
                        knows_endangered_fruits TEXT,
                        endangered_fruits TEXT,
                        rescue_strategies TEXT,
                        community_needs TEXT
                    )''')
    conn.commit()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect('survey.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO survey (
                        name, email, phone, age, gender, education, occupation, household_size,
                        speaks_indigenous_language, language, agriculture_main_income,
                        income_percentage, crops, crop_area, production_volume, production_value,
                        waste_percentage, has_fruit_trees, fruit_trees, consume_fruits,
                        consume_method, unused_fruits, tree_age, planted_trees, other_fruits_consumed,
                        other_fruits_source, childhood_fruits, childhood_fruit_sources,
                        consume_childhood_fruits, reasons_not_consuming, reasons_fruits_not_known,
                        knows_endangered_fruits, endangered_fruits, rescue_strategies,
                        community_needs
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', data)
    conn.commit()
    conn.close()

def main():
    st.title("Encuesta: Conocimiento de Frutos Subutilizados de la Región")
    st.write("Este cuestionario es para fines académicos y la información será tratada de forma confidencial.")

    create_table()

    # Captura de datos
    name = st.text_input("Nombre del entrevistado")
    email = st.text_input("Correo electrónico")
    phone = st.text_input("Teléfono")
    age = st.text_input("Edad (quinquenal como en INEGI)")
    gender = st.selectbox("Género", ["", "Femenino", "Masculino"])
    education = st.selectbox("Escolaridad", ["", "Sin escolaridad", "Primaria", "Secundaria", "Bachillerato", "Universidad", "Posgrado"])
    occupation = st.text_area("Ocupación (señalar sus diversas ocupaciones por orden de importancia)")
    household_size = st.number_input("Número de personas que viven en su vivienda", min_value=1, step=1)
    speaks_indigenous_language = st.radio("¿En su hogar, hablan alguna lengua indígena?", ["Si", "No"])
    language = "" if speaks_indigenous_language == "No" else st.text_input("¿Cuál lengua indígena?")

    agriculture_main_income = st.radio("¿La actividad agrícola es su principal fuente de ingresos?", ["Si", "No"])
    income_percentage = st.selectbox("¿Qué porcentaje de los ingresos familiares derivan de esta actividad?", ["", "20%", "30%", "40%", "50%", "Más del 50%"])

    crops = st.text_area("¿Cuáles son los cultivos que produce? (ejemplo: naranja, cítricos, granos)")
    crop_area = st.text_input("Extensión de tierra (Hectáreas)")
    production_volume = st.text_input("Volumen de producción (Ton, Kg)")
    production_value = st.text_input("Valor de la producción")
    waste_percentage = st.text_input("¿Cuánto de esta producción se convierte en residuos (%)?")

    has_fruit_trees = st.radio("¿Cuenta con árboles frutales en su vivienda?", ["Si", "No"])
    fruit_trees = "" if has_fruit_trees == "No" else st.text_area("¿Cuáles árboles frutales tiene?")

    consume_fruits = "" if has_fruit_trees == "No" else st.radio("¿Consume estos frutos?", ["Si", "No"])
    consume_method = "" if consume_fruits == "No" else st.text_area("¿Cómo los consume? (ejemplo: frescos, en conserva, en preparaciones tradicionales)")
    unused_fruits = "" if consume_fruits == "Si" else st.text_area("¿Qué sucede con los frutos que no consume?")

    tree_age = st.selectbox("Aproximadamente cuánto tiempo tienen la mayor parte de los árboles frutales en su vivienda", ["", "1-10 años", "10-20 años", "Más de 20 años"])
    planted_trees = st.radio("¿Usted sembró estos árboles frutales?", ["Si, todos", "Si, una parte de ellos", "No"])

    other_fruits_consumed = st.text_area("¿Qué otros frutos consume que no se encuentren en los árboles frutales de su vivienda?")
    other_fruits_source = st.text_area("¿Cómo obtiene esos frutos que consume y no produce en su vivienda?")

    childhood_fruits = st.text_area("¿Qué frutos consumía en la infancia?")
    childhood_fruit_sources = st.text_area("¿Cómo obtenía su familia esos frutos que consumía en su infancia?")

    consume_childhood_fruits = st.radio("¿Actualmente consume todos los frutos que consumía en su infancia?", ["Si", "No"])
    reasons_not_consuming = "" if consume_childhood_fruits == "Si" else st.text_area("¿Cuáles son las razones por las que no consume los mismos frutos de su infancia?")
    reasons_fruits_not_known = st.text_area("Razones por las que algunos frutos de la región ya no se conocen y no se consumen")

    knows_endangered_fruits = st.radio("¿Sabía que existen frutos considerados como subutilizados y en peligro de extinción en la Península de Yucatán?", ["Si", "No"])
    endangered_fruits = "" if knows_endangered_fruits == "No" else st.text_area("¿Cuáles considera que son esos frutos subutilizados y en peligro de extinción?")

    rescue_strategies = st.text_area("¿Qué estrategias podría proponer para el rescate de estos frutos subutilizados y en peligro de extinción?")
    community_needs = st.text_area("Menciona algunas necesidades de la comunidad que requieren pronta atención")

    # Guardar datos
    if st.button("Guardar Respuesta"):
        data = (name, email, phone, age, gender, education, occupation, household_size,
                speaks_indigenous_language, language, agriculture_main_income, income_percentage,
                crops, crop_area, production_volume, production_value, waste_percentage,
                has_fruit_trees, fruit_trees, consume_fruits, consume_method, unused_fruits,
                tree_age, planted_trees, other_fruits_consumed, other_fruits_source, childhood_fruits,
                childhood_fruit_sources, consume_childhood_fruits, reasons_not_consuming,
                reasons_fruits_not_known, knows_endangered_fruits, endangered_fruits,
                rescue_strategies, community_needs)

        insert_data(data)
        st.success("¡Encuesta guardada exitosamente!")

if __name__ == "__main__":
    main()
