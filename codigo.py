import pandas as pd

# Ruta del archivo Excel
ruta_archivo = r"C:\Users\usuario\Desktop\Documentos, tareas de carlos. Con respecto a la universidad\excel para trabajo final.xlsx"

try:
    # Leer el archivo Excel en un DataFrame
    df = pd.read_excel(ruta_archivo, engine='openpyxl')
    
    # Mostrar las primeras filas del archivo
    print("Primeras filas del archivo Excel:")
    print(df.head())  # Muestra las primeras 5 filas
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta especificada: {ruta_archivo}")
except Exception as e:
    print(f"Ocurrió un error al procesar el archivo: {e}")

    print("Nombres de las columnas actuales:")
print(df.columns)



import pandas as pd

# Ruta del archivo Excel
ruta_archivo = r"C:\Users\usuario\Desktop\Documentos, tareas de carlos. Con respecto a la universidad\excel para trabajo final.xlsx"

try:
    # Cargar el archivo Excel
    df = pd.read_excel(ruta_archivo, engine='openpyxl')

    # Cambiar los nombres de todas las columnas
    nuevos_nombres = ["Nombre del pais","año","escala de vida","PBI","apoyo social","vida sana","esperanza de vida","libertad de toma de decisiones","generosidad","percepción de corrupción","afecto positivo","afecto negativo"]  # Ajusta los nombres
    df.columns = nuevos_nombres

    # Mostrar el DataFrame con las nuevas columnas
    print("DataFrame con columnas renombradas:")
    print(df.head())

   

