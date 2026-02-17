"""
Pantalla Virtual de Front Desk - Sistema de Gestión.
Actividad 6.2 - Ejercicio de programación 2.
"""
import os
import json
from hotel import Hotel, Customer, Reservation


def mostrar_menu():
    """Muestra el menú interactivo al usuario."""
    print("\n" + "=" * 30)
    print(" HOTEL FRONT DESK SYSTEM ")
    print("=" * 30)
    print("H - Crear/Modificar Hotel")
    print("C - Crear Cliente")
    print("R - Crear Reservación")
    print("D - Consultar Información (Display)")
    print("X - Eliminar Registro")
    print("S - Salir")
    return input("Seleccione una opción: ").upper()


def ejecutar_consulta():
    """Maneja la lógica de consulta de datos (Opción D)."""
    msg = "¿Qué consultar? (H: Hotel, C: Cliente, R: Reserva): "
    tipo = input(msg).upper()
    id_busqueda = input("Ingrese el ID a buscar: ")
    prefijos = {"H": "hotel", "C": "customer", "R": "reservation"}

    if tipo not in prefijos:
        print("Tipo de consulta inválido.")
        return

    filename = f"{prefijos[tipo]}_{id_busqueda}.json"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f_handle:
            datos = json.load(f_handle)
            print("\n--- Datos Encontrados ---")
            print(json.dumps(datos, indent=4))
    else:
        print(f"Error: No se encontró el registro ID {id_busqueda}.")


def main():
    """Ciclo principal de interacción de la terminal."""
    while True:
        choice = mostrar_menu()
        try:
            if choice == 'H':
                hid = input("ID del Hotel: ")
                nom = input("Nombre: ")
                hab = input("Habitaciones: ")
                Hotel(hid, nom, hab).save()
                print("Operación de Hotel exitosa.")
            elif choice == 'C':
                cid = input("ID del Cliente: ")
                nom = input("Nombre completo: ")
                Customer(cid, nom).save()
                print("Cliente guardado exitosamente.")
            elif choice == 'R':
                rid = input("ID Reservación: ")
                hid = input("ID Hotel: ")
                cid = input("ID Cliente: ")
                Reservation(rid, hid, cid).save()
                print("Reservación creada.")
            elif choice == 'D':
                ejecutar_consulta()
            elif choice == 'X':
                tipo = input("¿Qué eliminar? (H/C/R): ").upper()
                id_del = input("ID a eliminar: ")
                pref = {"H": "hotel", "C": "customer", "R": "reservation"}
                filename = f"{pref[tipo]}_{id_del}.json"
                if os.path.exists(filename):
                    os.remove(filename)
                    print("Registro eliminado físicamente.")
            elif choice == 'S':
                print("Cerrando sesión del sistema...")
                break
        except Exception as err:  # pylint: disable=broad-exception-caught
            # Req 5: Captura errores de entrada y continúa la ejecución
            print(f"Error detectado: {err}. El sistema continúa.")


if __name__ == "__main__":
    main()
