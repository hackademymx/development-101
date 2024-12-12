import json
import requests

def sincronizar_progreso(progreso_path, api_url):
    try:
        with open(progreso_path, 'r') as file:
            progreso = json.load(file)
        response = requests.post(api_url, json=progreso)
        if response.status_code == 200:
            print("Progreso sincronizado con éxito.")
        else:
            print("Error al sincronizar:", response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    PROGRESO_PATH = "progress/template_progreso.json"
    API_URL = "https://tu-servidor.com/subir_progreso"
    sincronizar_progreso(PROGRESO_PATH, API_URL)
