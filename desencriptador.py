# Importar el módulo de expresiones regulares
import re

# Función para agregar palabras clave a un archivo
def agregar_palabra_clave(palabra):
    with open("palabras_clave.txt", "a") as archivo:
        archivo.write(palabra + "\n")

# Función para cargar palabras clave desde un archivo
def cargar_palabras_clave():
    try:
        with open("palabras_clave.txt", "r") as archivo:
            palabras_clave = [line.strip() for line in archivo]
            return palabras_clave
    except FileNotFoundError:
        return []

# Función para desencriptar un mensaje
def desencriptar_mensaje(mensaje, palabras_clave):
    for palabra in palabras_clave:
        mensaje = mensaje.replace(palabra, "")
        # Utilizando la función sub() del módulo re para sustituir múltiples espacios con un solo espacio
        mensaje = re.sub(' +', ' ', mensaje)
    return mensaje

# Menú principal
while True:
    print("\nDesencriptador de Mensajes con Palabras Clave")
    print("1. Agregar palabra clave")
    print("2. Desencriptar mensaje")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        palabra_clave = input("Ingrese la palabra clave: ")
        agregar_palabra_clave(palabra_clave)
        print(f"Palabra clave '{palabra_clave}' agregada con éxito.")
    elif opcion == "2":
        mensaje = input("Ingrese el mensaje a desencriptar: ")
        palabras_clave = cargar_palabras_clave()
        mensaje_desencriptado = desencriptar_mensaje(mensaje, palabras_clave)
        print("Mensaje desencriptado: " + mensaje_desencriptado)
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
