"""
Módulo para el sistema de reservaciones.
Actividad 6.2 - Ejercicio de programación 2.
"""
import json
import os


class Hotel:
    """Clase para manejar la información de los hoteles (Req 1.1)."""

    def __init__(self, hotel_id, name, rooms):
        """Inicializa los atributos del hotel."""
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms

    def display_information(self):
        """Muestra la información del hotel en consola (Req 2.1.c)."""
        print(f"Hotel ID: {self.hotel_id} | Nombre: {self.name} | "
              f"Habitaciones: {self.rooms}")

    def save_to_file(self):
        """Guarda la información en un archivo JSON (Persistencia)."""
        filename = f"hotel_{self.hotel_id}.json"
        data = {'id': self.hotel_id, 'name': self.name, 'rooms': self.rooms}
        with open(filename, "w", encoding="utf-8") as file_handle:
            json.dump(data, file_handle)

    @staticmethod
    def load_from_file(filename):
        """Carga datos de un archivo con manejo de errores (Req 5)."""
        try:
            with open(filename, "r", encoding="utf-8") as file_handle:
                return json.load(file_handle)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"Error al procesar {filename}: {error}. Continuando...")
            return None


class Customer:
    """Clase para manejar la información de los clientes (Req 1.2)."""

    def __init__(self, customer_id, name):
        """Inicializa el cliente."""
        self.customer_id = customer_id
        self.name = name

    def save_to_file(self):
        """Guarda los datos del cliente en JSON."""
        filename = f"customer_{self.customer_id}.json"
        with open(filename, "w", encoding="utf-8") as file_handle:
            json.dump({'id': self.customer_id, 'name': self.name}, file_handle)


class Reservation:
    """Clase para las reservaciones (Req 1.3)."""

    def __init__(self, res_id, customer_id, hotel_id):
        """Crea una reservación vinculando cliente y hotel."""
        self.res_id = res_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def save_to_file(self):
        """Persistencia de reservación."""
        filename = f"reservation_{self.res_id}.json"
        with open(filename, "w", encoding="utf-8") as file_handle:
            json.dump(self.__dict__, file_handle)
