import subprocess
import requests
import sys

# Configuración del usuario y del backend
USER_MAIL = ""  # Cambiar según sea necesario, agrega tu correo
ENDPOINT_URL = "https://apiprogreso.hackademy.lat/submit-progress"  # Cambia la URL según tu backend

def ejecutar_pruebas(archivo_prueba):
    """
    Ejecuta pytest en el archivo de prueba especificado.
    """
    try:
        resultado = subprocess.run(
            ["pytest", archivo_prueba, "--tb=short", "--disable-warnings"],
            stdout=subprocess.PIPE,
            text=True
        )
        print(resultado.stdout)
        return resultado.returncode, resultado.stdout
    except Exception as e:
        print(f"Error al ejecutar las pruebas: {e}")
        sys.exit(1)

def enviar_progreso(exercise_name, status, score):
    """
    Envía el progreso al backend.
    """
    payload = {
        "user_mail": USER_MAIL,
        "exercise_name": exercise_name,
        "status": status,
        "score": score
    }

    try:
        response = requests.post(ENDPOINT_URL, json=payload)
        if response.status_code == 201:
            print("✅ Progreso registrado exitosamente.")
        else:
            print(f"❌ Error al registrar progreso: {response.json().get('error')}")
    except Exception as e:
        print(f"❌ Error al conectar con el backend: {e}")

def main():
    """
    Ejecuta las pruebas y envía los resultados si todas las pruebas pasan.
    """
    if len(sys.argv) != 3:
        print("Uso: python main.py <carpeta_ejercicio> <nombre_ejercicio>")
        sys.exit(1)

    carpeta_ejercicio = sys.argv[1]
    nombre_ejercicio = sys.argv[2]

    archivo_prueba = f"ejercicios/{carpeta_ejercicio}/test_solucion.py"

    print(f"🔍 Ejecutando pruebas para el ejercicio: {nombre_ejercicio}...")
    return_code, pytest_output = ejecutar_pruebas(archivo_prueba)

    if return_code == 0:
        print("✅ Todas las pruebas pasaron.")
        enviar_progreso(nombre_ejercicio, status="completado", score=100)
    else:
        print("❌ Las pruebas fallaron. Por favor, revisa los errores e intenta nuevamente.")
        print(pytest_output)

if __name__ == "__main__":
    main()
