import json
import os

class Hotel:
    """Clase para manejar la información de los hoteles."""
    def __init__(self, hotel_id, name, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms

    def save_to_file(self):
        """Guarda la información del hotel en un archivo JSON."""
        data = {'id': self.hotel_id, 'name': self.name, 'rooms': self.rooms}
        with open(f"hotel_{self.hotel_id}.json", "w") as f:
            json.dump(data, f)
