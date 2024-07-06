from PRINCIPAL_IVAN_TORRES_SECCION_005 import *


def saludo():
    print("hola bienvenido a supermercados TODOAHORRO")

def menu():
    opciones = [
        "Registrar cliente",
        "Listar clientes registrados",
        "Registrar compra",
        "Listar compras por cliente",
        "Salir",
    ]

    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

def registrar_cliente(PC):
    nombre = input("Ingrese primer nombre del cliente: ").upper()
    apellido = input("Ingrese primer apellido del cliente: ").upper()
    correo = input("Ingrese primer correo electronico").upper()
    
    print("Ingrese el correo del cual se inscribe: ")
    for i, s in enumerate(correo):
        print(f"{i+1}. {s}")
    
    num_correo = input("Ingrese la sede de inscripción: ")
    if num_correo == "1":
        correo = "nombre\t\t\tcorreo"
    elif num_correo == "2":
        correo = "apellido\t\t\tcorreo"

    id_cliente = len(PC) + 1

    PC.append(
        {
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "ID": id_cliente,
            "compras": []
        }
    )

    print("\nSE HA AGREGADO UN CLIENTE NUEVO A LA PC!\n")


def listar_clientes(PC):
    print("\nLos clientes registrados son:\n")
    print("Nombre\t\t\tID\t\tcorreo")
    for cliente in PC:
        print(f'{cliente["nombre"]} {cliente["apellido"]}\t\t{cliente["ID"]}\t\t{cliente["correo"]}')

    print("\nListado creado con éxito!\n")



def registrar_compra(PC):
    id = int(input("Ingrese el ID de la compra: "))

    for cliente in PC:
        if cliente["ID"] == id:
            fecha = input("Ingrese fecha de entrenamiento (AAAA-MM-DD): ")
            costo = int(input("Ingrese : "))
            cliente["asistencias"].append(
                {
                    "fecha": fecha,
                    "costo": costo
                }
            )
            print(f'\nSe ha agregado una asistencia a {cliente["nombre"]} {cliente["apellido"]}.')
            break
        else:
            print(f"El cliente de ID = {id} no existe.")
        

def listar_compras_por_cliente(PC):
    id = int(input("Ingrese el ID del cliente que asiste: "))

    for cliente in PC:
        if cliente["ID"] == id:
            texto = f"IDcliente: {id}\n"
            texto += f'NOMBRE cliente: {cliente["nombre"]} {cliente["apellido"]}\n'
            texto += f"Fecha de Asistencia\t\t\n"

            tiempo_total = 0
            for asistencia in cliente["asistencias"]:
                texto += f'{asistencia["fecha"]}\t\t{asistencia["correo"]}\n'
                tiempo_total += asistencia["tiempo"]

            texto += f'TIEMPO TOTAL DE compra: {tiempo_total} minutos'

            with open(f"ASISTENCIAS_ID_{id}.txt", "w", encoding='utf-8') as archivo:
	            archivo.write(texto)

            print("ARCHIVO CREADO")

            break






        
    
