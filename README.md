
---

# T6.2 Sistema de Reservaciones - Hotel Front Desk

**A01105695**

**José Luis Lorenzo Augusto Galíndez Vences**

Este proyecto consiste en un sistema de gestión de reservaciones basado en consola, diseñado para demostrar la implementación de abstracciones orientadas a objetos, persistencia de datos en archivos JSON y estándares de calidad de software mediante pruebas unitarias y análisis estático.

## 📌 Propósito del Ejercicio

El objetivo principal es aplicar los principios de **Gestión de Configuración de Software (SCM)** y **Aseguramiento de Calidad (QA)**. Se busca garantizar la integridad del sistema mediante:

* **Abstracción de Datos:** Modelado de entidades reales (Hotel, Cliente, Reservación).
* **Persistencia:** Manejo de ciclo de vida de datos en almacenamiento físico.
* **Verificación y Validación:** Uso de pruebas unitarias para alcanzar una cobertura superior al 85%.

Aqui una muestra de la interfaz con la que se pueden crear los hoteles, reservaciones y clientes para hacer las pruebas:

---

## 📂 Contenido del Repositorio

| Archivo | Descripción |
| --- | --- |
| `hotel.py` | **Lógica de Negocio:** Contiene las clases `Hotel`, `Customer` y `Reservation` con sus métodos de persistencia (`save`, `delete`). |
| `main.py` | **Interfaz de Usuario:** Implementa el menú interactivo y el manejo de excepciones para asegurar la continuidad del sistema (Req 5). |
| `test_hotel.py` | **Suite de Pruebas:** Casos de prueba unitarios desarrollados con el módulo `unittest`, aplicando `setUp` y `tearDown` para aislamiento. |


<img width="406" height="286" alt="Screenshot 2026-02-20 at 9 06 09 p m" src="https://github.com/user-attachments/assets/f4ec86fd-52a4-446f-9cad-81771dc49659" />

---

## 🛠 Verificación de Calidad

Para cumplir con los estándares de **Calidad de Software**, se utilizan las siguientes herramientas:

### 1. Pruebas Unitarias (`unittest`)

Se han diseñado 7 casos de prueba que ejercitan cada unidad del sistema en aislamiento.

```bash
python3 test_hotel.py

```

### 2. Cobertura de Código (`coverage`)

Siguiendo el **Req 4**, el sistema debe mantener al menos un 85% de cobertura de líneas.

```bash
# Ejecutar medición
coverage run -m unittest test_hotel.py

# Generar reporte
coverage report -m

```

> **Resultado Actual:** 100% de cobertura en la lógica de negocio (`hotel.py`).

Aqui se pueden ver los resultados de unitest y coverage hechos satisfactoriamente:

<img width="812" height="303" alt="Screenshot 2026-02-20 at 10 03 42 p m" src="https://github.com/user-attachments/assets/27ea9cc1-8b4f-48f5-9a6b-a16ca818fe05" />



### 3. Análisis Estático (`Pylint` & `Flake8`)

Para asegurar la adherencia a los estándares **PEP-8** :

```bash
# Verificar calidad del código (Meta: 10/10)
pylint hotel.py main.py

# Verificar estilo y sintaxis
flake8 hotel.py main.py

```
Aqui se muestran los resultados de verificación con calificación de 10.0 para pylint y sin warnins en flake 8 para cada uno de los programas contenidos



<img width="674" height="272" alt="Screenshot 2026-02-20 at 9 51 40 p m" src="https://github.com/user-attachments/assets/41bcf01d-2d57-49b8-9007-0e8ce2f94c09" />



---

## ⚠️ Manejo de Errores (Req 5)

El sistema está diseñado para ser robusto. Cualquier error en la entrada de datos o archivos corruptos es capturado por un bloque `try-except` global en `main.py`, notificando al usuario en consola pero permitiendo que la ejecución continúe sin interrupciones.

---

