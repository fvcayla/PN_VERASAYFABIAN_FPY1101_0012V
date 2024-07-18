import random 
import csv

trabajadores = [
    {"nombre": "Juan Pérez"},
    {"nombre": "María García"},
    {"nombre": "Carlos López"},
    {"nombre": "Ana Martínez"},
    {"nombre": "Pedro Rodríguez"},
    {"nombre": "Laura Hernández"},
    {"nombre": "Miguel Sánchez"},
    {"nombre": "Isabel Gómez"},
    {"nombre": "Francisco Díaz"},
    {"nombre": "Elena Fernández"}
]

def asignar_sueldos():
    for trabajador in trabajadores:
        trabajador["sueldo"] = random.randint(300000, 2500000)
        
def clasificar_sueldos():
    rangos = {"Bajo": 0, "Medio": 0, "Alto": 0}
    for empleado in empleados:
        sueldo = empleado["sueldo"]
        if sueldo <= 1000000:
            rangos["Bajo"] += 1
        elif sueldo <= 1800000:
            rangos["Medio"] += 1
        else:
            rangos["Alto"] += 1
    print("Clasificación de sueldos:")
    for rango, cantidad in rangos.items():
        print(f"- {rango}: {cantidad}")

# Función para clasificar un sueldo en un rango
def clasificar_rango(sueldo):
    if sueldo <= 1000000:
        return "Bajo"
    elif sueldo <= 1800000:
        return "Medio"
    else:
        return "Alto"

# Función para realizar descuentos
def aplicar_descuentos():
    for empleado in empleados:
        if empleado["sueldo"] > 1800000:
            descuento = empleado["sueldo"] * 0.1
            empleado["sueldo"] -= descuento
            print(f"Sueldo de {empleado['nombre']} con descuento: ${empleado['sueldo']:,}")

# Función para ver estadísticas
def ver_estadisticas():
    sueldos = [empleado["sueldo"] for empleado in empleados]
    promedio = sum(sueldos) / len(sueldos)
    máximo = max(sueldos)
    mínimo = min(sueldos)
    print(f"Sueldo promedio: ${promedio:,}")
    print(f"Sueldo máximo: ${máximo:,}")
    print(f"Sueldo mínimo: ${mínimo:,}")

# Función para generar reporte CSV
def generar_reporte_csv():
    with open("reporte_sueldos.csv", "w") as archivo:
        # Escribir encabezados
        archivo.write("Nombre,Cargo,Sueldo,Rango,Descuento\n")

        # Escribir datos de cada empleado
        for empleado in empleados:
            nombre = empleado["nombre"]
            cargo = empleado["cargo"]
            sueldo = empleado["sueldo"]
            rango = clasificar_rango(sueldo)
            descuento = 0 if sueldo <= 1800000 else empleado["sueldo"] * 0.1
            archivo.write(f"{nombre},{cargo},{sueldo:,},{rango},{descuento:,}\n")

# Menú principal
def menu_principal():
    while True:
        print("\nMenú principal:")
        print("1. Asignar sueldos")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte CSV")
        print("5. Salir del programa")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            asignar_sueldos()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            generar_reporte_csv()
        elif opcion == "5":
            print("Saliendo del programa...")
            print("Desarrollado por Fabian Verasay")
            print("RUT 15.744.089-6")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Iniciar el programa
menu_principal()        