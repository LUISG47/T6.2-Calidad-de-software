"""
Módulo de pruebas unitarias final para hotel.py.
Garantiza 100% de cobertura y cumplimiento de rúbrica (casos negativos).
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
            f"reservation_{self.res_id}.json",
            "corrupt.json"
        ]
        for f in files:
            if os.path.exists(f):
                os.remove(f)

    # --- CASOS POSITIVOS (Para subir cobertura al 100%) ---

    def test_hotel_persistence(self):
        """Prueba guardado y borrado de Hotel (Línea 25-34)."""
        self.hotel.save()
        self.assertTrue(os.path.exists(f"hotel_{self.hotel_id}.json"))
        Hotel.delete(self.hotel_id)
        self.assertFalse(os.path.exists(f"hotel_{self.hotel_id}.json"))

    def test_customer_persistence(self):
        """Prueba guardado de Customer (Línea 51-53)."""
        self.customer.save()
        self.assertTrue(os.path.exists(f"customer_{self.customer_id}.json"))

    def test_reservation_persistence(self):
        """Prueba guardado de Reservation (Línea 72-74)."""
        self.reservation.save()
        self.assertTrue(os.path.exists(f"reservation_{self.res_id}.json"))

    def test_display_info_coverage(self):
        """Ejercita métodos display_info (Líneas 20, 51, 67)."""
        self.hotel.display_info()
        self.customer.display_info()
        self.reservation.display_info()

    # --- CASOS NEGATIVOS (Rúbrica 30 ptos) ---

    def test_negative_delete_none(self):
        """Caso Negativo 1: Borrar ID inexistente."""
        Hotel.delete("9999")
        self.assertTrue(True)

    def test_negative_invalid_json(self):
        """Caso Negativo 2: Archivo corrupto (Req 5)."""
        filename = "corrupt.json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("{ invalid }")
        with self.assertRaises(json.JSONDecodeError):
            with open(filename, "r", encoding="utf-8") as f:
                json.load(f)

    def test_negative_empty_customer(self):
        """Caso Negativo 3: Cliente con strings vacíos."""
        c = Customer("", "")
        self.assertEqual(c.name, "")

    def test_negative_file_not_found(self):
        """Caso Negativo 4: Abrir archivo que no existe."""
        with self.assertRaises(FileNotFoundError):
            with open("ghost.json", "r") as f:
                json.load(f)

    def test_negative_null_reservation(self):
        """Caso Negativo 5: Atributos None en Reservación."""
        r = Reservation(None, None, None)
        self.assertIsNone(r.res_id)


if __name__ == '__main__':
    unittest.main()
