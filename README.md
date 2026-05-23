------------------------
PROCESO ANTES DEL CODEAR
------------------------
Este proceso consta de un orden:
1.  verificamos si python esta instalado con con ayuda de la interfaz de comandos(terminal,powershell,gitbash)
con el siguiente comando python --version y a la ves verificamos si el gestor de paquetes eesta presente con el comando pip --version.

2.  creamos la carpeta en la que se contendra este proyecto.
3. creamos el archivo main.py.
4. accedemos a la interfaz de comandos en VC para crear el entorno virtual con el siguiente comando python -m venv venv.
5. una vez hecho lo anterior activamos el entorno virtual con el siguiente comando .\venv\Scripts\activate.
6. ahora instalaremos la tecnologia (framework) FastAPI con el comando pip install "fastapi{standard}".
7. y verificamos la lista de paquetes instalados dentro del entorno con el comando pip list.
8. y ejecutamos con el comando fastapi dev main.py.

---------------------------
DESARROLLO DE LOS ENDPOINTS
---------------------------
En esta parte se explicaran conceptos de la POO sus pilares, fastapi y como se relaciona con el desarrollo de los ejercicios.

1. ¿Qué es la POO?
La Programación Orientada a Objetos (POO) es una forma de programar usando objetos y clases. Sirve para organizar mejor el código y hacerlo más fácil de entender.

2. Pilares de la POO

 Encapsulamiento
Permite proteger la información y controlar el acceso a los datos.

 Herencia
Permite que una clase herede características de otra para reutilizar código.

 Polimorfismo
Permite usar un mismo método de diferentes maneras.

  Abstracción
Permite mostrar solo la información importante y ocultar detalles innecesarios.

3. ¿Qué es FastAPI?
FastAPI es un framework de Python que sirve para crear APIs rápidas y sencillas.

4. ¿Qué hace el código?

5. Importa FastAPI

from fastapi import FastAPI

6. Crea la aplicación

nombre_pro_clientes = FastAPI()

7. Crea una ruta principal

@nombre_pro_clientes.get("/")
def mensaje():
    return{"mensaje": "Este es el proyecto de clientes a desarrollar"}

Esta ruta muestra un mensaje principal.

8. Crea una ruta de clientes

@nombre_pro_clientes.get("/clientes")
def clientes():
    clientes = ["Jorge Alejandro Torres Paez",
    "Sara Jasmin Cruz Calderon",
    "Santiago Buitrago Goyeneche",
    "Jonny Guerrero",
    "Eddy Santiago Caro"]
    return[clientes]

Esta ruta muestra una lista de clientes.

9. Relación entre POO y FastAPI
La POO ayuda a organizar el código y FastAPI permite crear APIs de forma rápida. Juntos ayudan a desarrollar aplicaciones más ordenadas y fáciles de mejorar.
