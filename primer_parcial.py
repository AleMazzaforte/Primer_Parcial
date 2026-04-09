# Primer parcial Programacion 1 

# Mensaje de bienvenida
print("Bienvenido al sistema de control de stock Ferreteria 'El Cosito' ")

# Declaración de variables

herramientas = ["a", "b", "c"]
existencias = [1, 3, 30]

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
            print("Stock total")
            for i in range(len(herramientas)):
                print(f"{herramientas[i]} - {existencias[i]}")
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
        case "4":
            print("Stock por producto")
            herramienta_unidad = input("Ingrese la herramiente ").strip().lower()
                # Aca valido la herramienta 
            while not herramienta_unidad.isalpha() or herramienta_unidad not in herramientas:
                print("Valor incorrecto. Ingrese solo letras y asegúrese que la herramienta ya esté ingresada")
                herramienta = input("Ingrese la herramienta ").strip().lower()
            indice = herramientas.index(herramienta_unidad)
            print(f"Hay {existencias[indice]} unidades de {herramientas[indice]}")
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
        case "5":
            # Listar productos con existencia 0
            print("Los pruductos que no hay en existencia son:")
            for i in range(len(herramientas)):
                if existencias[i] == 0:
                    print(f"{herramientas[i]}")
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
        case "6":
            # Alta de nuevo producto
            alta = input("Ingrese el producto nuevo ").strip().lower()
            while not alta.isalpha():
                alta = input("Ingrese solo letras para el producto nuevo ").strip().lower()

            cant = input("Ingrese la cantidad ").strip()
            while not cant.isdigit():
                cant = input("Valor incorrecto para la cantidad, ingrese solo número mayor que 0 ")
            cant = int(cant)
            # isalpha me condiciona a que el numero de cant sea sin signo por lo tanto es positivo pero como en el 
            # enunciado pide que valor de existencia negativo se lo trate igual que a nombre repetido o vacio lo 
            # incluyo en el while y en el if 
            while alta in herramientas or alta == "" or cant < 0:
                if not alta.isalpha():
                    print("Para la herramienta debe elegir solo letras")
                elif alta in herramientas:
                    print("La herramienta ya existe en la base de datos")
                elif cant < 0:
                    print("La cantidad no puede ser un número negativo")
                else:
                    print("El nombre de la herramienta no puede estar vacío")
                print("Por favor elija nuevamente un número del menú")
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
            herramientas.append(alta)
            existencias.append(cant)
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
            
        case "7":
            # Actualizacion de Stock
            operacion = input("""
                Ingrese un número para vender o comprar.
                    1. Ventas.
                    2. Compras.
                    3. Volver al menú principal.
                """).strip()
            # Valido el número para elegir comprar o vender
            while not operacion.isdigit() or operacion not in ["1", "2", "3"]:
                print("Valor incorrecto, ingrese solo número del 1 al 3")
                operacion = input("""
                Ingrese un número para vender o comprar.
                    1. Ventas.
                    2. Compras.
                    3. Volver al menú principal.
                """).strip()
            while True:
                match operacion:
                    case "1":
                        producto_a_vender = input("Ingrese el producto que quiere vender ").strip().lower()
                        while producto_a_vender.isdigit():
                            print("Valor incorrecto, debe ingresar solo letras.")
                            producto_a_vender = input("Ingrese el producto que quiere vender ").strip().lower()

                        
                        if producto_a_vender in herramientas:
                            indice = herramientas.index(producto_a_vender)
                            print(indice)
                            if existencias[indice] == 0:
                                print(f"No hay unidades en existencia de {producto_a_vender}")
                            else:
                                print(f"Hay en existencia {existencias[indice]} unidades")
                                cantidad_a_vender = input("Cuantas unidades quiere vender? ").strip()
                                # Valido que ingrese número y que sea != de 0
                                while not cantidad_a_vender.isdigit() or cantidad_a_vender == "0":
                                    print("Valor incorrecto, ingrese solo números enteros mayores que 0")
                                    cantidad_a_vender = input("Cuantas unidades quiere vender? ").strip()
                                # Convierto a int para comparar con existencia
                                cantidad_a_vender= int(cantidad_a_vender)     
                                # Valido que no se venda mas de lo que hay
                                print(type(existencias[indice]))
                                while cantidad_a_vender > existencias[indice]:
                                    print("Valor incorrecto, la cantidad a vender no puede superar la existencia")
                                    cantidad_a_vender = input("Cuantas unidades quiere vender? ").strip()
                                # Vuelvo a validar que haya ingresado número y != de 0
                                    while not cantidad_a_vender.isdigit() or cantidad_a_vender == "0":
                                        print("Valor incorrecto, ingrese solo números enteros mayores que 0")
                                        cantidad_a_vender = input("Cuantas unidades quiere vender? ").strip()
                                         # Vuelvo a convertir a int
                                    cantidad_a_vender= int(cantidad_a_vender) 
                                
                                existencias[indice] = int(existencias[indice]) - cantidad_a_vender
                                print("Venta exitosa!!")
                        else:
                            print("El producto a vender no está en la base de datos, por favor ingréselo primero en el ítem 6 del menú principal.")                            

                        # Pido menú principal
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
                        break

                            
                    case "2":
                        # Compras
                        producto_comprado = input("Ingrese el producto a comprar. ").strip().lower()
                        # Valido que el producto sean caracteres alfabeticos
                        while not producto_comprado.isalpha():
                            print("Valor incorrecto, ingrese solo letras")
                            producto_comprado = input("Ingrese el producto a comprar. ").strip().lower()
                        # Valido que el producto ya esté cargado
                        if producto_comprado in herramientas:
                            # Pido la cantidad y la valido
                            cantidad_comprada = input("Ingrese la cantidad comprada ").strip()
                            
                            while not cantidad_comprada.isdigit() or cantidad_comprada == "0":
                                print("Valor incorrecto, ingrese solo números")
                                cantidad_comprada = input("Ingrese la cantidad comprada ").strip()
                            cantidad_comprada = int(cantidad_comprada)
                            # Busco en indice de la herramienta para actualizar la existencia
                            indice = herramientas.index(producto_comprado)
                            existencias[indice] = existencias[indice] + cantidad_comprada
                            print("Compras guardadas exitosamente.") 
                            # print(herramientas)
                            # print(existencias)
                        else:
                            print("El producto comprado no está en la base de datos, por favor ingréselo en el item 6 del menú principal.")

                        # Pido menú principal
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
                        break
                                                        
                    case "3":
                        # Pido menú principal
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
                            break
                        break
                    
        case "10":
            print("Gracias por usar nuestro sistema, lo esperamos nuevamente cuando lo necesite.")
            break

        


