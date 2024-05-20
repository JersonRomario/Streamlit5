import streamlit as st
import pandas as pd
import io

def read_file(file):
    data = pd.read_csv(file, header=None, names=["Empleado", "HorasTrabajadas"])
    return data

def calculate_total_hours(data):
    total_hours = data.groupby("Empleado")["HorasTrabajadas"].sum().reset_index()
    return total_hours

def save_total_hours(data):
    output = io.StringIO()
    for index, row in data.iterrows():
        output.write(f"{row['Empleado']}, {row['HorasTrabajadas']}\n")
    return output.getvalue().encode('utf-8')

def main():
    st.title("Informe de Horas Totales Trabajadas por Empleado")

    uploaded_file = st.file_uploader("Sube tu archivo de registro de horas de trabajo (TXT)", type=["txt"])

    if uploaded_file is not None:
        data = read_file(uploaded_file)
        st.write("Datos cargados:")
        st.dataframe(data)

        total_hours = calculate_total_hours(data)
        st.write("Horas totales trabajadas por empleado:")
        st.dataframe(total_hours)

        save_button = st.button("Guardar informe en archivo")

        if save_button:
            output = save_total_hours(total_hours)
            st.download_button(label="Descargar informe",
                               data=output,
                               file_name="horas_totales_trabajadas.txt",
                               mime="text/plain")
            st.success("Archivo guardado con éxito como 'horas_totales_trabajadas.txt'.")

if __name__ == "__main__":
    main()
