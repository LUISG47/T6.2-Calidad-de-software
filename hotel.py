"""
Módulo para generar el control de información del hotel.
Actividad 6.2 - Ejercicio de programación 2.
"""
import json


class Hotel:
    """Clase para manejar la información de los hoteles."""

    def __init__(self, hotel_id, name, rooms):
        """Inicializa los atributos del hotel."""
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms

    def display_information(self):
        """Muestra la información del hotel en consola."""
        print(f"Hotel ID: {self.hotel_id}")
        print(f"Nombre: {self.name}")
        print(f"Habitaciones: {self.rooms}")

    def save_to_file(self):
        """Guarda la información del hotel en un archivo JSON."""
        data = {'id': self.hotel_id, 'name': self.name, 'rooms': self.rooms}
        filename = f"hotel_{self.hotel_id}.json"
        with open(filename, "w", encoding="utf-8") as file_handle:
            json.dump(data, file_handle)
