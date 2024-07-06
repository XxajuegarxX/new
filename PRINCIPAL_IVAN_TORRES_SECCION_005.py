from FUNCIONES_IVAN_TORRES_SECCION_005  import *

PC = [
    {
        "nombre": "Juanito",
        "apellido": "Perez",
        "correo electronico": "Juan.perez@yopmail.com",
        "ID": 1,
        "Compras":[
            {
              "Monto toal": "Total compra inicial",
        "Puntos acumulados": "450 PESOS",
        "fecha": [{"fecha": "2024-07-01", }, {"fecha": "2024-07-03", }]  
            }
        ]
    }
]

print("¡Bienvenido a la cadena de supermercados TODOAHORRO y sus registros")

while True:

    # LOS PRINTS DEL MENU 
    menu()

    # ELEGIR UNA OPCIÓN
    opcion = input("Ingrese la opción a ejecutar: ")

    if opcion == "1":
        registrar_cliente(PC)

    elif opcion == "2":
        registrar_compra(PC)

    elif opcion == "3":
        listar_compras_por_cliente(PC)

    elif opcion == "4":
        print("HASTA LA PRÓXIMA!")
        break 

    else:
        print("%$&$! HAGALO OTRA VEZ")
