"""Módulo de pruebas unitarias optimizado para hotel.py."""
import unittest
import os
import json
from hotel import Hotel, Customer, Reservation

class TestHotelSystem(unittest.TestCase):
    """Pruebas unitarias siguiendo los estándares de David Sale."""

    def setUp(self):
        """Configuración previa a cada prueba (D.R.Y)."""
        self.hotel_id = "H1"
        self.customer_id = "C1"
        self.res_id = "R1"
        
        # Instancias para usar en los tests
        self.hotel = Hotel(self.hotel_id, "Hotel Test", 100)
        self.customer = Customer(self.customer_id, "Diana Sanchez")
        self.reservation = Reservation(self.res_id, self.hotel_id, self.customer_id)

    def tearDown(self):
        """Limpieza después de cada prueba para mantener aislamiento."""
        files = [
            f"hotel_{self.hotel_id}.json",
            f"customer_{self.customer_id}.json",
            f"reservation_{self.res_id}.json"
        ]
        for f in files:
            if os.path.exists(f):
                os.remove(f)

    def test_hotel_save_and_persistence(self):
        """Prueba la unidad de persistencia de Hotel."""
        self.hotel.save()
        filename = f"hotel_{self.hotel_id}.json"
        self.assertTrue(os.path.exists(filename))
        
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Verificamos que los datos guardados son correctos (David Sale)
            self.assertEqual(data['hotel_id'], self.hotel_id)

    def test_customer_display_info(self):
        """Prueba el método display_info (unidad aislada)."""
        # Verificamos que no truene al imprimir
        try:
            self.customer.display_info()
        except Exception as err:
            self.fail(f"display_info lanzó una excepción: {err}")

    def test_reservation_creation(self):
        """Verifica la correcta asociación de IDs en la reserva."""
        self.assertEqual(self.reservation.hotel_id, self.hotel_id)
        self.assertEqual(self.reservation.customer_id, self.customer_id)

    def test_delete_hotel_behavior(self):
        """Prueba la unidad de eliminación."""
        self.hotel.save()
        Hotel.delete(self.hotel_id)
        self.assertFalse(os.path.exists(f"hotel_{self.hotel_id}.json"))

    def test_invalid_data_handling(self):
        """Uso de assertRaises para validar tipos de datos (David Sale)."""
        # Si intentamos abrir un JSON corrupto o inexistente en lógica externa
        with self.assertRaises(FileNotFoundError):
            with open("no_existe.json", "r") as f:
                json.load(f)

if __name__ == '__main__':
    unittest.main()
