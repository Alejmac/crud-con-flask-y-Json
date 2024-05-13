from flask import Flask, render_template, request, redirect, url_for, send_file,abort
from users import añadir_usuario, obtener_usuarios

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',titulo="Proyecto IOT",active="home")

@app.route('/users')
def mostrar_usuarios():
    usuarios = obtener_usuarios()
    return render_template('users.html', usuarios=usuarios)

@app.route('/adduser')
def adduser():
    return render_template('adduser.html',titulo="Proyecto IOT",active="usuarios")

@app.route('/insertar_usuario', methods=['POST'])
def insert_user():
    if request.method == 'POST':
        # Recupera los datos del formulario
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        cargo = request.form['cargo']
        empresa = request.form['empresa']
        calle = request.form['calle']
        numeroExt = request.form['numeroExt']
        numeroInt = request.form['numeroInt']
        colonia = request.form['colonia']
        municipio = request.form['municipio']
        estado = request.form['estado']
        codigoPostal = request.form['codigopostal']
        telefono = request.form['telefono']
        email = request.form['email']
        fechaNac = request.form['fechanac']
        añadir_usuario(nombre,apellido1,apellido2,cargo,empresa,calle,numeroExt,numeroInt,colonia,municipio,estado,codigoPostal,telefono,email,fechaNac)
    return redirect(url_for('index'))

@app.route('/edit_user', methods=['POST'])
def edit_user():
    # Recibir el usuario que vas a editar

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=80)