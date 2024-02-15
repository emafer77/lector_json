import json

# Abre el archivo JSON en modo lectura
with open('datos.json', 'r') as archivo_json:
    # Carga el contenido del archivo JSON en un diccionario
    datos = json.load(archivo_json)

# Accede a los datos como lo harías con un diccionario
nombre = datos['nombre']
edad = datos['edad']
ciudad = datos['ciudad']

# Imprime los datos
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")