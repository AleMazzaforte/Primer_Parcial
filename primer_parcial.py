# Primer parcial Programacion 1 

# Mensaje de bienvenida
print("Bienvenido al sistema de control de stock Ferreteria 'El Cosito' ")

# Declaración de variables

herramientas = []
existencias = []

# Comienza el programa mostrando el menu y solicitando seleccion de actividad a realizar

accion = input("""
    Ingrese un número para elegir la actividad a realizar.
        1. Carga de herramientas.
        2. Carga de existencias.
        3. Visualizar el inventario.
        4. Consulta de stock por producto.
        5. Reporte de quiebre de stock.
        6. Alta de nuevo producto.
        7. Actualizacion de stock.
            Venta o compra.
        10. Para salir del programa. 
    """).strip()

# Validacion de número del menú

while not accion.isdigit() and accion not in ["1", "2", "3", "4", "5", "6", "7", "10"]:
    print("El valor ingresado es incorrecto. Por favor ingrese solamente un número del menú")
    accion = input("""
        Ingrese un número para elegir la actividad a realizar.
            1. Carga de herramientas.
            2. Carga de existencias.
            3. Visualizar el inventario.
            4. Consulta de stock por producto.
            5. Reporte de quiebre de stock.
            6. Alta de nuevo producto.
            7. Actualizacion de stock.
                Venta o compra.
            10. Para salir del programa. 
        """).strip()
    
# Empieza el programa propiamente dicho

# Valido que herramientas tenga al menos 1 valor
if len(herramientas) == 0 and accion == "2":
    print("No existen herramientas dadas de alta. Pirmero ingrese las herramientas y luego las cantidades.")
    accion = "1"
    

while accion != 10:
    match accion:
        case "1": # Ingresar herramientas
            print("Módulo de carga de herramientas")
            while True:
                herramienta = input("Ingrese la herramienta. Para volver al menú ingrese Salir ").strip().lower()
                # print(f"Valor: '{herramienta}'")
                # print(f"Largo: {len(herramienta)}")
                if herramienta == "salir":
                    # Vuelvo a solicitar elección de menu 
                    accion = input("""
                        Ingrese un número para elegir la actividad a realizar.
                            1. Carga de herramientas.
                            2. Carga de existencias.
                            3. Visualizar el inventario.
                            4. Consulta de stock por producto.
                            5. Reporte de quiebre de stock.
                            6. Alta de nuevo producto.
                            7. Actualizacion de stock.
                                Venta o compra.
                            10. Para salir del programa. 
                        """).strip()
                    # Vuelvo a validar
                while not accion.isdigit() and accion not in ["1", "2", "3", "4", "5", "6", "7", "10"]:
                    print("El valor ingresado es incorrecto. Por favor ingrese solamente un número del menú")
                    accion = input("""
                        Ingrese un número para elegir la actividad a realizar.
                            1. Carga de herramientas.
                            2. Carga de existencias.
                            3. Visualizar el inventario.
                            4. Consulta de stock por producto.
                            5. Reporte de quiebre de stock.
                            6. Alta de nuevo producto.
                            7. Actualizacion de stock.
                                Venta o compra.
                            10. Para salir del programa. 
                        """).strip()
                    break
                    # Aca valido la herramienta 
                while not herramienta.isalpha() or herramienta in herramientas:
                    print("Valor incorrecto. Ingrese solo letras y sin repetir herramienta ya ingresada")
                    herramienta = input("Ingrese la herramienta ").strip().lower()
                # Guardo la herramienta
                if herramienta != "salir":
                    herramientas.append(herramienta)
                break            
        case "2": # Agregar stock            
            print("Agregue el stock inicial para cada herramienta")
            # Recorro la lista de herramientas pidiendo la cantidad correspondiente
            for i in herramientas:
                cantidad = input(f"{i}: ").strip()
                while not cantidad.isdigit():
                    print("Ingrese solo números")
                    cantidad = input(f"{i}: ").strip()
                # Guardo la cantidad de acuerdo al indice y convierto a int 
                existencias.append(int(cantidad))
            # Vuelvo a solicitar elección de menu 
            accion = input("""
                Ingrese un número para elegir la actividad a realizar.
                    1. Carga de herramientas.
                    2. Carga de existencias.
                    3. Visualizar el inventario.
                    4. Consulta de stock por producto.
                    5. Reporte de quiebre de stock.
                    6. Alta de nuevo producto.
                    7. Actualizacion de stock.
                        Venta o compra.
                    10. Para salir del programa. 
                """).strip()
                # Vuelvo a validar
            while not accion.isdigit() and accion not in ["1", "2", "3", "4", "5", "6", "7", "10"]:
                print("El valor ingresado es incorrecto. Por favor ingrese solamente un número del menú")
                accion = input("""
                    Ingrese un número para elegir la actividad a realizar.
                        1. Carga de herramientas.
                        2. Carga de existencias.
                        3. Visualizar el inventario.
                        4. Consulta de stock por producto.
                        5. Reporte de quiebre de stock.
                        6. Alta de nuevo producto.
                        7. Actualizacion de stock.
                            Venta o compra.
                        10. Para salir del programa. 
                    """).strip()

        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "10":
            pass
        


