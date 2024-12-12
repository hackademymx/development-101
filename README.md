# Curso de Introducción a la Programación con Python

Bienvenido al curso de introducción a la programación. Aquí encontrarás los notebooks y ejercicios necesarios para aprender desde cero.

## Requisitos
- **Python 3.8 o superior**
Puedes descargar python desde [Python](https://www.python.org/downloads/) donde podrás seleccionar tu sistema operativo.
En caso de usar Windows sigue los siguientes pasos:
![imagen](https://github.com/user-attachments/assets/e1263869-975b-498c-a3c9-1c2381a926ff)

### Instalación Python en windows

La instalación en Windows es sencilla, el propio instalador de Python sirve de guia para instalar todas las dependencias y requisitos. Python se puede descargar gratis para windows [aquí](https://www.python.org/downloads/windows/).
![imagen](https://github.com/user-attachments/assets/6524ea13-5456-4345-ab75-5a8b0048b192)
![imagen](https://github.com/user-attachments/assets/c8fbfcc1-a26e-452b-9b4b-12989a6a628a)
![imagen](https://github.com/user-attachments/assets/c9ee8c07-2d4c-4232-b64d-c5b6ddb65ce9)

Es importante seleccionar que Python se incluya en el path para facilitar la ejecución de módulos desde consola.

De esta forma se ha instalado el intérprete de Python y el IDE simple IDLE, el cual permite realizar los primeros programas en Python.

### Instalar en Linux

Python se encuentra instalado por defecto en la mayoría de distribuicioes de linux, pero quizas la versión instalada no es la que se desea.

Para instalar una versión diferente en linux se puede buscar en el gestor de dependencias y paquetes del sistema por la versión específica a instalar, o se puede instalar directamente desde el código fuente compilando la versión específica.

```
# Ubuntu (apt-get)
$ sudo apt-get update
$ sudo apt-get install python3.9

# Centos/Fedora (yum)
$ sudo yum install gcc openssl-devel bzip2-devel libffi-devel
## Instalación desde código fuente
$ cd /tmp
$ wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
$ tar xzf Python-3.9.0.tgz
$ cd Python-3.9.0
$ sudo ./configure --enable-optimizations
$ sudo make altinstall
```
Cuando se instala una nueva versión a nivel de sistema es importante utilizar make altinstall en vez de make install para instalar de forma alternativa a la versión instalada y utilizada en el sistema.

### Instalar en MacOS
Instalar Python usando el gestor de paquetes brew utilizando los siguientes comandos en una consola.

```
# instalar brew
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# instalar python
$ brew install python
```
- **Visual Studio Code** con las extensiones:
  - Python
  - Jupyter

Instalar Visual Studio Code, lo puedes descargar desde aquí dependiendo de tu sistema operativo: [Visual Studio Code](https://code.visualstudio.com/download)

### Instalar Extensiones
Al abrir Visual Studio Code podrás ir al menú principal -> Preferencias -> **Extensiones**

![Menú principal VS Code](https://github.com/user-attachments/assets/eb7076c2-91a2-484a-9678-f26a79d6421a)
![Captura de pantalla 2024-12-11 a la(s) 3 25 04 p m  (2)](https://github.com/user-attachments/assets/98cfa4ed-4330-4294-90b1-a109060533c0)
![Captura de pantalla 2024-12-11 a la(s) 3 25 08 p m  (2)](https://github.com/user-attachments/assets/3eecffc2-3863-4847-98bf-0e18cb831aa9)

Se abrirá una barra lateral con un campo de búsqueda en el cual escribirás "Python" e instalarás el paquete verificado por Microsoft
![Captura de pantalla 2024-12-11 a la(s) 3 25 26 p m  (2)](https://github.com/user-attachments/assets/ba2940b2-ebda-435c-b4be-52346a44a4d4)

Harás lo mismo con la extensión "Jupyter"
![Captura de pantalla 2024-12-11 a la(s) 3 25 56 p m  (2)](https://github.com/user-attachments/assets/34e2c632-9414-4cfd-8fb7-b6ab3905cd7f)


## Instrucciones de configuración
1. **Repositorio**
Si no tienes una cuenta GitHub puedes crear una o solamente descargar este repositorio en formato Zip, al descargarlo guardalo en tu carpeta Dcomentos y descomprimelo.
Si tienes una cuenta GitHub **Clona este repositorio** desde tu línea de comandos, primero te debes de posicionar en la carpeta donde quieres clonar el repositorio:
    ```bash
    git clone https://github.com/hackademymx/development-101
    cd development-101
    ```
2. Abre tu Visual Studio Code, ve al menú inicio -> abrir carpeta y abre la carpeta del curso.

![Captura de pantalla 2024-12-11 a la(s) 4 00 14 p m  (2)](https://github.com/user-attachments/assets/9fd9d903-5565-404c-b0d3-7e2c8a9d03b5)

Ya que tengas cargada la carpeta ve al menú terminal -> nueva terminal

![Captura de pantalla 2024-12-11 a la(s) 4 01 40 p m  (2)](https://github.com/user-attachments/assets/9bf908ea-733c-4d20-a356-663080e109fa)

3. **Crea y activa un entorno virtual** escribiendo los siguientes comando en la terminal que acabas de abrir:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa env\Scripts\activate
    ```

4. **Instala las dependencias** escribiendo los siguientes comando en la terminal que acabas de abrir:
    ```bash
    pip install -r requirements.txt
    ```

5. **Abre un notebook en Visual Studio Code**:
    - Navega a la carpeta `notebooks`.
    - Abre un archivo `.ipynb`.
    - Asegúrate de seleccionar el entorno virtual como intérprete.
      Al ejecutar, por primera vez, una celda de código te pedirá seleccionar el interprete.
      **Debes de seleccionar el del ambiente virtual:**
      ![Captura de pantalla 2024-12-11 a la(s) 4 51 45 p m  (2)](https://github.com/user-attachments/assets/faf884bf-53f7-4ce0-9b12-d9df014f5e74)


    


## Progreso
Para llevar un control de tu avance, utiliza el archivo `progress/template_progreso.json` como base. Completa el archivo con tus datos y sincronízalo con el servidor usando `sincronizar_progreso.py`.

¡Buena suerte!
