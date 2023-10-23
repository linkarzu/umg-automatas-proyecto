# Importar la clase Flask, la función render_template, y el módulo request del paquete Flask
from flask import Flask, render_template, request

# Importar las funciones del script desencriptador existente
import desencriptador  

# Inicializar la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la URL raiz ('/') y especificar los métodos que va a manejar
@app.route('/', methods=['GET', 'POST'])
def index():
    # Verificar si el método de solicitud HTTP es POST
    if request.method == 'POST':
        # Recuperar el dato 'message' del envío del formulario
        message = request.form.get('message')
        
        # Usar la función cargar_palabras_clave del script desencriptador para obtener las palabras clave
        palabras_clave = desencriptador.cargar_palabras_clave()
        
        # Usar la función desencriptar_mensaje del script desencriptador para obtener el mensaje desencriptado
        desencriptado = desencriptador.desencriptar_mensaje(message, palabras_clave)
        
        # Renderizar la plantilla 'index.html' y pasarle el mensaje desencriptado
        return render_template('index.html', desencriptado=desencriptado, message=message)

    # Si el método de solicitud no es POST, simplemente renderizar la plantilla 'index.html'
    return render_template('index.html')

# Ejecutar la aplicación Flask sólo si este script se ejecuta directamente (no se importa)
if __name__ == "__main__":
    # Ejecutar el servidor de desarrollo de Flask con el modo de depuración habilitado
    app.run(debug=True)
