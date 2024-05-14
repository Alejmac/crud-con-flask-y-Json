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

# # Ejemplo de uso:
# añadir_usuario("John", "Doe", "", "Developer", "ABC Inc.", "123 Main St", "1", "", "Downtown", "City", "State", "12345", "555-1234", "john@example.com", "2000-01-01")


# # Verificar que el usuario fue añadido correctamente 
def obtener_usuarios():
    # Verificar si el archivo JSON existe
    if not os.path.exists('users.json'):
        return []  # Si el archivo no existe, retornar una lista vacía

    # Abrir el archivo JSON y cargar su contenido actual
    with open('users.json', 'r') as file:
        usuarios_exist = json.load(file)

    return usuarios_exist

#funcion para editar un usuario en el archivo JSON
def editar_usuario(nombre, apellido1=None, apellido2=None, cargo=None, empresa=None, calle=None, numeroExt=None, numeroInt=None, colonia=None, municipio=None, estado=None, codigoPostal=None, telefono=None, email=None, fechaNac=None):
    # Verificar si el archivo JSON existe
    if not os.path.exists('users.json'):
        return  # Si el archivo no existe, no hay nada que editar

    # Abrir el archivo JSON y cargar su contenido actual
    with open('users.json', 'r') as file:
        usuarios_exist = json.load(file)

    # Buscar al usuario en la lista de usuarios
    for usuario in usuarios_exist:
        if usuario['nombre'] == nombre:
            # Si se encontró al usuario, actualizar sus datos
            if apellido1 is not None:
                usuario['apellido1'] = apellido1
            if apellido2 is not None:
                usuario['apellido2'] = apellido2
            if cargo is not None:
                usuario['cargo'] = cargo
            if empresa is not None:
                usuario['empresa'] = empresa
            if calle is not None:
                usuario['calle'] = calle
            if numeroExt is not None:
                usuario['numeroExt'] = numeroExt
            if numeroInt is not None:
                usuario['numeroInt'] = numeroInt
            if colonia is not None:
                usuario['colonia'] = colonia
            if municipio is not None:
                usuario['municipio'] = municipio
            if estado is not None:
                usuario['estado'] = estado
            if codigoPostal is not None:
                usuario['codigoPostal'] = codigoPostal
            if telefono is not None:
                usuario['telefono'] = telefono
            if email is not None:
                usuario['email'] = email
            if fechaNac is not None:
                usuario['fechaNac'] = fechaNac
            break

    # Escribir el contenido actualizado de vuelta al archivo JSON
    with open('users.json', 'w') as file:
        json.dump(usuarios_exist, file, indent=4)

