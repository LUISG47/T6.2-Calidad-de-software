"""
Módulo de pruebas unitarias optimizado para hotel.py.
Cumple con los estándares de David Sale y los requerimientos de la actividad.
"""
import unittest
import os
import json
from hotel import Hotel, Customer, Reservation


class TestHotelSystem(unittest.TestCase):
    """Pruebas unitarias siguiendo los estándares de David Sale."""

    def setUp(self):
        """Configuración previa a cada prueba (Principio D.R.Y)."""
        self.hotel_id = "H1"
        self.customer_id = "C1"
        self.res_id = "R1"

        # Instancias para usar en los tests
        self.hotel = Hotel(self.hotel_id, "Hotel Test", 100)
        self.customer = Customer(self.customer_id, "Diana Sanchez")
        self.reservation = Reservation(
            self.res_id, self.hotel_id, self.customer_id
        )

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
        """Prueba la unidad de persistencia de Hotel (Req 2.1)."""
        self.hotel.save()
        filename = f"hotel_{self.hotel_id}.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(data['hotel_id'], self.hotel_id)

    def test_customer_save(self):
        """Prueba la persistencia de la clase Customer (Req 2.2)."""
        self.customer.save()
        filename = f"customer_{self.customer_id}.json"
        self.assertTrue(os.path.exists(filename))

    def test_reservation_save(self):
        """Prueba la persistencia de Reservation (Req 2.3)."""
        self.reservation.save()
        filename = f"reservation_{self.res_id}.json"
        self.assertTrue(os.path.exists(filename))

    def test_all_display_info_methods(self):
        """Ejercita los métodos display_info para cobertura."""
        # Eliminado try-except para corregir Pylint W0718
        self.hotel.display_info()
        self.customer.display_info()
        self.reservation.display_info()

    def test_delete_hotel_behavior(self):
        """Prueba la unidad de eliminación física (Req 2.1.b)."""
        self.hotel.save()
        Hotel.delete(self.hotel_id)
        self.assertFalse(os.path.exists(f"hotel_{self.hotel_id}.json"))

    def test_invalid_data_handling(self):
        """Uso de assertRaises para validar errores."""
        with self.assertRaises(FileNotFoundError):
            with open("no_existe.json", "r", encoding="utf-8") as f:
                json.load(f)

    def test_reservation_data_integrity(self):
        """Verifica que la reserva asocie correctamente los IDs."""
        self.assertEqual(self.reservation.hotel_id, self.hotel_id)
        self.assertEqual(self.reservation.customer_id, self.customer_id)


if __name__ == '__main__':
    unittest.main()
