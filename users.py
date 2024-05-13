import json
import os

def añadir_usuario(nombre, apellido1, apellido2, cargo, empresa, calle, numeroExt, numeroInt, colonia, municipio, estado, codigoPostal, telefono, email, fechaNac):
    # Crear el diccionario de usuario
    usuario = {
        'nombre': str(nombre),
        'apellido1': str(apellido1), 
        'apellido2': str(apellido2),
        'cargo': str(cargo),
        'empresa': str(empresa),
        'calle': str(calle),
        'numeroExt': str(numeroExt),
        'numeroInt': str(numeroInt),
        'colonia': str(colonia),
        'municipio': str(municipio),
        'estado': str(estado),
        'codigoPostal': str(codigoPostal),
        'telefono': str(telefono),
        'email': str(email),
        'fechaNac': str(fechaNac)
    }

    # Verificar si el archivo JSON existe
    if not os.path.exists('users.json'):
        # Si el archivo no existe, inicializarlo con una lista que contenga solo el nuevo usuario
        with open('users.json', 'w') as file:
            json.dump([usuario], file, indent=4)
    else:
        try:
            # Abrir el archivo JSON y cargar su contenido actual
            with open('users.json', 'r') as file:
                usuarios_exist = json.load(file)
        except json.decoder.JSONDecodeError:
            # Si el archivo JSON está vacío o no tiene el formato JSON esperado, inicializarlo con una lista que contenga solo el nuevo usuario
            with open('users.json', 'w') as file:
                json.dump([usuario], file, indent=4)
            return

        # Agregar el nuevo usuario a la lista de usuarios
        usuarios_exist.append(usuario)

        # Escribir el contenido actualizado de vuelta al archivo JSON
        with open('users.json', 'w') as file:
            json.dump(usuarios_exist, file, indent=4)

# Ejemplo de uso:
añadir_usuario("John", "Doe", "", "Developer", "ABC Inc.", "123 Main St", "1", "", "Downtown", "City", "State", "12345", "555-1234", "john@example.com", "2000-01-01")
