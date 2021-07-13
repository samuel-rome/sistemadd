# mis funciones
from tabulate import tabulate


def read_file(filename):
    my_file = open(filename)
    return my_file.readlines()


def store_data_component(data, c_id, name, price):
    data.append({
        "Apellido": c_id,
        "Nombre": name,
        "Nota - Promedio": price
    })
    return data


def print_table(data):
    print(tabulate(data, headers="keys", tablefmt="fancy_grid"))


def store_data_alumnos(data, numerodelista, c_id, name, price):
    data.append({
        "N°": numerodelista,
        "Apellido": c_id,
        "Nombre": name,
        "Nota-Promedio": price
    })
    return data

def store_data_alumnos_c(data, numerodelista, c_id, name, price):
    data.append({
        "N°": numerodelista,
        "Apellido": c_id,
        "Nombre": name,
        "Nota-Promedio": price
    })
    return data

def store_data_alumnos_ci(data, numerodelista, c_id, name, price):
    data.append({
        "N°": numerodelista,
        "Apellido": c_id,
        "Nombre": name,
        "Nota-Promedio": price
    })
    return data


