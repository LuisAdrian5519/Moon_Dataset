import os

# Obtener la carpeta actual
carpeta_base = os.getcwd()  # Usa esta línea para la carpeta actual

# O usa esta línea si quieres una carpeta específica:
# carpeta_base = r"C:\Users\Owner\Downloads\robs.v10i.yolov12 - Copy"

# Contador de archivos eliminados
contador = 0

# Recorrer todas las carpetas y subcarpetas
for raiz, _, archivos in os.walk(carpeta_base):
    for archivo in archivos:
        if archivo.startswith("2024") and archivo.endswith((".jpg", ".txt")):
            ruta_archivo = os.path.join(raiz, archivo)
            try:
                os.remove(ruta_archivo)
                print(f"Eliminado: {ruta_archivo}")
                contador += 1
            except Exception as e:
                print(f"Error al eliminar {ruta_archivo}: {e}")

# Mostrar resultado final
if contador == 0:
    print("No se encontraron archivos para eliminar.")
else:
    print(f"Proceso terminado. Se eliminaron {contador} archivo(s).")
