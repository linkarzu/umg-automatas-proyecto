
# Imagen referencia

<div align="center">
    <img src="https://res.cloudinary.com/daqwsgmx6/image/upload/v1698271959/Dev/python/automatas-desencriptador/desencriptador-grupo5.png" width="600">
</div>

# Curso

- Autómatas y Lenguajes Formales
- Grupo 5
- UMG 2023
- Segundo semestre
- Ing. Efrain Marroquin

# Descripción

Desencriptador que reciba de entrada un mensaje de texto
que dentro del mensaje tiene palabras CLAVE y al quitar
las palabras clave se queda el mensaje.

Por ejemplo, si se tienen las siguientes palabras clave:
TALADRO, HAMBRUNA, EDEN, DES, CABAÑA

Y se ingresa el mensaje:
TU HAMBRUNA PU TALADRO EDE EDEN DES SHACER CABAÑA LO

Al quitar las palabras clave queda el mensaje:
TU PU EDES SHACER LO.

El proyecto consiste en que tienen que generar un archivo de entrada para el caso
que seleccionen para que lo lean y realicen la funcionalidad indicada.

# Instrucciones para correr en windows

## Instalación de python

Descargamos python de https://www.python.org/downloads/, vamos a instalar la version 3.12.0 que es la última al día de hoy

- En la 1er ventana de instalación, seleccionar la opción que dice `add python.exe to PATH`
- Dar click en `Disable path length limit`, si aparece

Al terminar la instalación, confirmar que ambos python y pip estén instalados

```bash
python --version
pip --version
```

Acá podemos ver que sí están instlados

```bash
C:\Users\krishna>python --version
Python 3.12.0
C:\Users\krishna>pip --version
pip 23.2.1 from
C:\Users\krishna\AppData\Local\Programs\Python\Python312\Lib\site-pac
kages\pip (python 3.12)
```


## Instalación de git

Descargamos git de la página https://gitforwindows.org/

- Instalamos utilizando todas las opciones por defecto
- Configuré `Visual Studio Code` como el editor de texto por defecto
- El branch name lo cambié a `main`
- Para el PATH environment seleccioné `Git from the command line and also from 3rd-party software`

Al haber instalado git ahora abro `Git CMD` y realizo la configuración básica con estos 2 comandos

- Cambiar a tu usuario y correo electrónico

```bash
git config --global user.name "Christian Arzu"
git config --global user.email "myemail@gmail.com"
```

Verifico que los datos se configuraron correctamente

```bash
git config --global user.name
git config --global user.email
```

## Clonar repo

Ahora clono la repo de git

```bash
mkdir github
cd github
git clone https://github.com/linkarzu/umg-automatas-proyecto
```

Me cambio a ese directorio clonado

```bash
cd umg-automatas-proyecto
```

## Activar venv e instalar flask

Voy a crear un ambiente virtual para instalar ahí las dependencias, en nuestro caso flask que nos va a servir para conectar con el frontend

De primero creamos el ambiente virtual  

- Podemos escoger cualquier nombre para el ambiente virtual, en este caso usé `myenv`

```bash
python -m venv myenv
```

Activamos el ambiente virtual

- Si el ambiente se activó correctamente deberíamos de ver `myenv` en nuestro prompt

```bash
myenv\Scripts\activate
```

Ahora que el ambiente virtual está activado, instalo flask

```bash
pip install Flask
```

Ahora que flask está instalado en el ambiente virtual, vamos a correr la aplicación de flask llamada app.py dentro del código

- Las primeras 2 líneas son variables de entorno que seteamos
- Si el servidor se inició correctamente nos va a mostrar la URL para poder ver la página
- accesamos a la página utilizando la url mostrada, en nuestro caso `127.0.0.1:5000`

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

Las palabras clave se cambian únicamente en el backend, en el archivo `palabras_clave.txt`

