"""Script de ejecución principal con argumentos de terminal."""
import sys
from hotel import Hotel

def main():
    """Función principal para probar archivos JSON uno por uno."""
    # Verificamos si el usuario pasó un nombre de archivo
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
        print(f"--- Verificando archivo: {nombre_archivo} ---")
        
        # Cargamos los datos usando el método con manejo de errores (Req 5)
        datos = Hotel.load_from_file(nombre_archivo)
        
        if datos:
            try:
                # Creamos el objeto con los datos cargados
                h = Hotel(datos['id'], datos['name'], datos['rooms'])
                # Mostramos la info (Req 2.1.c)
                h.display_information()
                print("Verificación exitosa.")
            except (KeyError, TypeError):
                print(f"Error: El formato de {nombre_archivo} es inválido.")
    else:
        print("Uso: python3 main.py <nombre_archivo.json>")
        print("Ejemplo: python3 main.py test_hotel_0.json")

if __name__ == "__main__":
    main()
