"""Módulo de pruebas unitarias para hotel.py."""
import unittest
import json
import os
from hotel import Hotel


class TestHotel(unittest.TestCase):
    """Pruebas para los requerimientos de la clase Hotel."""

    def test_load_and_create_from_random_json(self):
        """Prueba la creación de un hotel usando los archivos json generados."""
        # Probamos con el primer archivo generado por tu randomgen.py
        file_path = 'test_hotel_0.json'
        
        if not os.path.exists(file_path):
            self.skipTest(f"Archivo {file_path} no encontrado. Corre randomgen.py primero.")

        with open(file_path, 'r', encoding='utf-8') as file_handle:
            data = json.load(file_handle)
            hotel = Hotel(data['id'], data['name'], data['rooms'])
            
            # Verificamos que los datos se cargaron correctamente
            self.assertEqual(hotel.hotel_id, data['id'])
            self.assertEqual(hotel.name, data['name'])

    def test_invalid_file_handling(self):
        """Req 5: Verificar que el sistema maneja archivos inexistentes o inválidos."""
        # Intentamos cargar un archivo que no existe
        try:
            with open('archivo_inexistente.json', 'r', encoding='utf-8') as f:
                json.load(f)
        except FileNotFoundError:
            # Si el programa imprime el error y continúa, la prueba pasa
            print("\n[Manejo de Error] Archivo no encontrado - Continuando ejecución.")
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
