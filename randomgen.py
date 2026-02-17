"""
Módulo para generar el control de información del hotel
Actividad 6.2 - Ejercicio de programación 2.
"""
import random
import json

def generate_test_data(num_files=5):
    """Genera archivos JSON con datos aleatorios para pruebas."""
    for i in range(num_files):
        data = {
            "id": i,
            "name": f"Hotel_Random_{random.randint(100, 999)}",
            "rooms": random.randint(10, 100)
        }
        with open(f"test_hotel_{i}.json", "w") as f:
            json.dump(data, f)
    print(f"Se generaron {num_files} archivos de prueba.")

if __name__ == "__main__":
    generate_test_data()
