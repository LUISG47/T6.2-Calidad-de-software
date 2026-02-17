"""Módulo de lógica para el Sistema de Reservaciones."""
import json
import os


class Hotel:
    """Clase Hotel con persistencia (Req 1.1)."""
    def __init__(self, hotel_id, name, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms

    def save(self):
        """Guarda el hotel en un archivo JSON (Req 2.1)."""
        with open(f"hotel_{self.hotel_id}.json", "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f)

    @staticmethod
    def load(hotel_id):
        """Carga un hotel desde su archivo."""
        filename = f"hotel_{hotel_id}.json"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return None


class Customer:
    """Clase Cliente con persistencia (Req 1.2)."""
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def save(self):
        """Guarda el cliente en JSON (Req 2.2)."""
        with open(f"customer_{self.customer_id}.json", "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f)


class Reservation:
    """Clase Reservación (Req 1.3)."""
    def __init__(self, res_id, hotel_id, customer_id):
        self.res_id = res_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id

    def save(self):
        """Guarda la reservación (Req 2.3)."""
        with open(f"reservation_{self.res_id}.json", "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f)
