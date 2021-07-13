import funciones

# CONTRASEÑA PARA EL MAESTRO
password = "1234"
# CONTRASEÑA PARA EL Estudiante
contrasena = "4321"
# CURO DE MATEMATICA
list_numer = funciones.read_file('MATEMATICA/numerodeorden.txt')
c_id = funciones.read_file('MATEMATICA/apellidos.txt')
c_names = funciones.read_file('MATEMATICA/alumnos.txt')
c_prices = funciones.read_file('MATEMATICA/nota.txt')
table_alumnos_data = []
for i in range(len(list_numer)):
    numerodelista = list_numer[i].strip()
    component_id = c_id[i].strip()
    name = c_names[i].strip()
    price = c_prices[i].strip()
    table_alumnos_data = funciones.store_data_alumnos(
        table_alumnos_data,
        numerodelista,
        component_id,
        name,
        price
    )

# CURSO DE COMUNICACION
list_numer = funciones.read_file('Comunicacion/numerodeorden-C.txt')
c_id = funciones.read_file('Comunicacion/apellidos-C.txt')
c_names = funciones.read_file('Comunicacion/alumnos-C.txt')
c_prices = funciones.read_file('Comunicacion/nota-C.txt')
table_alumnos_data_c = []
for i in range(len(list_numer)):
    numerodelista = list_numer[i].strip()
    component_id = c_id[i].strip()
    name = c_names[i].strip()
    price = c_prices[i].strip()
    table_alumnos_data_c = funciones.store_data_alumnos_c(
        table_alumnos_data_c,
        numerodelista,
        component_id,
        name,
        price
    )

# CURSO DE CIENCIAS
list_numer = funciones.read_file('Ciencias/numerodeorden-CI.txt')
c_id = funciones.read_file('Ciencias/apellidos-CI.txt')
c_names = funciones.read_file('Ciencias/alumnos-CI.txt')
c_prices = funciones.read_file('Ciencias/nota-CI.txt')
table_alumnos_data_ci = []
for i in range(len(list_numer)):
    numerodelista = list_numer[i].strip()
    component_id = c_id[i].strip()
    name = c_names[i].strip()
    price = c_prices[i].strip()
    table_alumnos_data_ci = funciones.store_data_alumnos_ci(
        table_alumnos_data_ci,
        numerodelista,
        component_id,
        name,
        price
    )

respuesta = input("  1 ➔ Ingresar como Maestro\n  2 ➔ Ingresar como Estudiante\n  3 ➔ Salir?\n  "
                  + str("Eliga la opcion: "))
while respuesta != "3":

    # Interfaz
    if respuesta == "1":
        print("=" * 36)
        intento = input("Introduce la contraseña: ")
        print("=" * 38)
        while intento != password:
            print("la contraseña no es correcta")
            print("=" * 38)
            intento = input("Intentalo otra vez: ")
            print("=" * 38)
        print(" -------> BIENVENIDO MAESTRO <-------")
        print("=" * 38)
        operation = input(
            '''Seleccione una opcion:\n [1] Ver Notas \n [2] Ingresar Notas \n [3] Elimar Notas\n [4] Volver al menu Principal\n ''' + str(
                "⁓⁓ "))
        print("=" * 36)
        while operation != "4":
            # OPCION 1 VER NOTAS
            if operation == "1":
                print("1.----> Matematica\n"
                      "2.----> Comunicacion\n"
                      "3.----> Ciencias")
                print("=" * 36)
                curso = int(input("--> Eliga una opcion --> 1, 2, 3\n"
                                  "⁓⁓ "))
                if curso == 1:
                    print("=" * 44)
                    funciones.print_table(table_alumnos_data)
                    # print("⬇" * 50)
                    print("=" * 36)
                if curso == 2:
                    print("=" * 36)
                    funciones.print_table(table_alumnos_data_c)
                    print("=" * 36)
                if curso == 3:
                    print("=" * 36)
                    funciones.print_table(table_alumnos_data_ci)
                    print("=" * 36)

            # OPCION 2 AGREGAR ALUMNOS/NOTAS
            if operation == "2":

                print("1.----> Matematica\n"
                      "2.----> Comunicacion\n"
                      "3.----> Ciencias")
                print("=" * 37)
                print(" -Eliga el curso para Agregar notas-")
                print("=" * 37)
                curso = int(input("--> Eliga una opcion --> 1, 2, 3\n"
                                  "⁓⁓ "))
                # INGRESAR NOTAS - Matematica
                if curso == 1:
                    print("=" * 44)
                    funciones.print_table(table_alumnos_data)
                    print("=" * 44)
                    input_numero = input("Ingrese el Siguiente numero de orden: ")
                    input_lastname = input("Ingrese Apellido: ")
                    input_name = input("Ingrese Nombre: ")
                    input_price = input("Ingrese Nota: ")
                    table_alumnos_data = funciones.store_data_alumnos(
                        table_alumnos_data,
                        input_numero,
                        input_lastname,
                        input_name,
                        input_price
                    )
                    funciones.print_table(table_alumnos_data)
                    # print("⬇" * 50)
                    print("=" * 36)
                # INGRESAR NOTAS - COMUNICACION
                if curso == 2:
                    print("=" * 44)
                    funciones.print_table(table_alumnos_data_c)
                    print("=" * 44)
                    input_numero = input("Ingrese el Siguiente numero de orden: ")
                    input_lastname = input("Ingrese Apellido: ")
                    input_name = input("Ingrese Nombre: ")
                    input_price = input("Ingrese Nota: ")
                    table_alumnos_data_c = funciones.store_data_alumnos(
                        table_alumnos_data_c,
                        input_numero,
                        input_lastname,
                        input_name,
                        input_price
                    )
                    funciones.print_table(table_alumnos_data_c)
                    # print("⬇" * 50)
                    print("=" * 36)
                # INGRESAR NOTAS - CIENCIAS
                if curso == 3:
                    print("=" * 44)
                    funciones.print_table(table_alumnos_data_ci)
                    print("=" * 44)
                    input_numero = input("Ingrese el Siguiente numero de orden: ")
                    input_lastname = input("Ingrese Apellido: ")
                    input_name = input("Ingrese Nombre: ")
                    input_price = input("Ingrese Nota: ")
                    table_alumnos_data_ci = funciones.store_data_alumnos(
                        table_alumnos_data_ci,
                        input_numero,
                        input_lastname,
                        input_name,
                        input_price
                    )
                    funciones.print_table(table_alumnos_data_ci)
                    # print("⬇" * 50)
                    print("=" * 36)

            # OPCION 3 ELIMINAR NOTAS
            if operation == "3":
                print("1.----> Matematica\n"
                      "2.----> Comunicacion\n"
                      "3.----> Ciencias")
                print("=" * 36)
                curso = int(input("--> Eliga una opcion --> 1, 2, 3\n"
                                  "⁓⁓ "))
                # MATEMATICA - DELETE
                if curso == 1:
                    funciones.print_table(table_alumnos_data)
                    print("=" * 36)
                    input_i = int(input("Put the number of element do you wish delete: "))
                    delate_w = input_i - 1
                    table_alumnos_data.pop(int(delate_w))
                    funciones.print_table(table_alumnos_data)
                # COMUNICACION - DELETE
                if curso == 2:
                    funciones.print_table(table_alumnos_data_c)
                    print("=" * 36)
                    input_i = int(input("Put the number of element do you wish delete: "))
                    delate_w = input_i - 1
                    table_alumnos_data_c.pop(int(delate_w))
                    funciones.print_table(table_alumnos_data_c)
                # CIENCIAS - DELETE
                if curso == 3:
                    funciones.print_table(table_alumnos_data_ci)
                    print("=" * 36)
                    input_i = int(input("Put the number of element do you wish delete: "))
                    delate_w = input_i - 1
                    table_alumnos_data_ci.pop(int(delate_w))
                    funciones.print_table(table_alumnos_data_ci)

            operation = input(
                '''Seleccione una opcion:\n [1] Ver Notas \n [2] Ingresar Notas \n [3] Eliminar Notas\n [4] Volver\n ''' + str(
                    "⁓⁓ "))

    # Metodos
    if respuesta == "2":
        print("=" * 36)
        intento = input("Introduce la contraseña: ")
        print("=" * 38)
        while intento != contrasena:
            print("la contraseña no es correcta")
            print("=" * 38)
            intento = input("Intentalo otra vez: ")
        print("=" * 38)
        print(" -------> BIENVENIDO ESTUDIANTE <-------")
        print("=" * 38)
        operation_alumno = input(
            '''Seleccione una opcion:\n [1] Ver Tus Promedios \n [2] Nota Para pasar \n [3] Volver \n  ''' + str("⁓⁓ "))
        print("=" * 36)
        while operation_alumno != "3":
            # OPCION 1 - VER LOS PROMEDIOS
            if operation_alumno == "1":
                from tabulate import tabulate

                table = [["Matematica", 14], ["Comunicacion", 15], ["Ciencias", 16]]
                headers = ["Curso", "Promedio"]
                print(tabulate(table, headers, tablefmt="fancy_grid"))
                print("=" * 36)

            if operation_alumno == "2":
                n1 = int(input("Primera Nota: "))
                n2 = int(input("Segunda Nota: "))
                n3 = int(input("Tercera Nota: "))
                operacion = (n1 * 0.25) + (n2 * 0.25) + (n3 * 0.25)
                nota_necesitada = 13 - operacion
                nota_final = nota_necesitada / 0.25
                nota_final_promedio = n1 + n2 + n3 + nota_final
                print("=" * 36)
                print("Tendras que sacar una calificacion minima de:", nota_final, str("para pasar el curso"))
                print("=" * 36)

            operation_alumno = input(
                '''Seleccione una opcion:\n [1] Ver Tus Promedios \n [2] Nota Para pasar \n [3] Volver \n  ''' + str(
                    "⁓⁓ "))

    # Volvemos a preguntar
    respuesta = input("  1 ➔ Ingresar como Maestro\n  2 ➔ Ingresar como Estudiante\n  3 ➔ Salir?\n  "
                  + str("Eliga la opcion: "))

print("=" * 36)
print("Saliendo...")
print("=" * 36)
print("=" * 36)
print("=" * 36)
print("=" * 36)
print("FIN")
