"""Pantalla Virtual de Front Desk - Sistema de Gestión."""
import os
from hotel import Hotel, Customer, Reservation

def menu():
    """Muestra el menú interactivo al usuario."""
    print("\n" + "="*30)
    print(" HOTEL FRONT DESK SYSTEM ")
    print("="*30)
    print("H - Crear/Modificar Hotel")
    print("C - Crear Cliente")
    print("R - Crear Reservación")
    print("D - Consultar Información (Display)")
    print("X - Eliminar Registro")
    print("S - Salir")
    return input("Seleccione una opción: ").upper()

def main():
    """Ciclo principal de interacción."""
    while True:
        choice = menu()
        try:
            if choice == 'H':
                hid = input("ID del Hotel: ")
                name = input("Nombre: ")
                rooms = input("Habitaciones: ")
                Hotel(hid, name, rooms).save()
                print("Operación exitosa.")

            elif choice == 'C':
                cid = input("ID del Cliente: ")
                name = input("Nombre completo: ")
                Customer(cid, name).save()
                print("Cliente guardado.")

            elif choice == 'R':
                rid = input("ID Reservación: ")
                hid = input("ID Hotel: ")
                cid = input("ID Cliente: ")
                Reservation(rid, hid, cid).save()
                print("Reservación creada.")

            elif choice == 'D':
                # Nueva lógica para consultar (Req 2.1.c, 2.2.c)
                tipo = input("¿Qué desea consultar? (H: Hotel, C: Cliente, R: Reserva): ").upper()
                id_busqueda = input("Ingrese el ID a buscar: ")
                
                prefix = {"H": "hotel", "C": "customer", "R": "reservation"}[tipo]
                filename = f"{prefix}_{id_busqueda}.json"
                
                if os.path.exists(filename):
                    import json
                    with open(filename, "r", encoding="utf-8") as f:
                        print(f"\nDatos encontrados:\n{json.dumps(json.load(f), indent=4)}")
                else:
                    print("Error: El archivo no existe.")

            elif choice == 'X':
                # Lógica para eliminar (Req 2.1.b, 2.2.b, 2.3.b)
                tipo = input("¿Qué eliminar? (H/C/R): ").upper()
                id_del = input("ID a eliminar: ")
                prefix = {"H": "hotel", "C": "customer", "R": "reservation"}[tipo]
                filename = f"{prefix}_{id_del}.json"
                if os.path.exists(filename):
                    os.remove(filename)
                    print("Registro eliminado físicamente.")
                else:
                    print("No se encontró el archivo.")

            elif choice == 'S':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")

        except Exception as e:
            # Req 5: Manejo de errores para que el sistema no se detenga
            print(f"Error detectado: {e}. El sistema continúa operando.")

if __name__ == "__main__":
    main()
