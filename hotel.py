"""
Módulo de lógica para el Sistema de Reservaciones.
Actividad 6.2 - Ejercicio de programación 2.
"""
import json
import os


class Hotel:
    """Clase Hotel con persistencia (Req 1.1)."""

    def __init__(self, hotel_id, name, rooms):
        """Inicializa los atributos del hotel."""
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms

    def display_info(self):
        """Muestra la información del hotel (Req 2.1.c)."""
        print(f"Hotel ID: {self.hotel_id} | Nombre: {self.name} | "
              f"Habitaciones: {self.rooms}")

    def save(self):
        """Guarda el hotel en un archivo JSON (Req 2.1)."""
        filename = f"hotel_{self.hotel_id}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f)

    @staticmethod
    def delete(hotel_id):
        """Elimina el archivo del hotel (Req 2.1.b)."""
        filename = f"hotel_{hotel_id}.json"
        if os.path.exists(filename):
            os.remove(filename)


class Customer:
    """Clase Cliente con persistencia (Req 1.2)."""

    def __init__(self, customer_id, name):
        """Inicializa el cliente."""
        self.customer_id = customer_id
        self.name = name

    def display_info(self):
        """Muestra datos del cliente (Req 2.2.c)."""
        print(f"Cliente ID: {self.customer_id} | Nombre: {self.name}")

    def save(self):
        """Guarda el cliente en JSON (Req 2.2)."""
        filename = f"customer_{self.customer_id}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f)


class Reservation:
    """Clase Reservación (Req 1.3)."""

    def __init__(self, res_id, hotel_id, customer_id):
        """Inicializa la reservación."""
        self.res_id = res_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id

    def display_info(self):
        """Muestra datos de la reserva."""
        print(f"Reserva: {self.res_id} | Hotel: {self.hotel_id} | "
              f"Cliente: {self.customer_id}")

    def save(self):
        """Guarda la reservación (Req 2.3)."""
        filename = f"reservation_{self.res_id}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f)
