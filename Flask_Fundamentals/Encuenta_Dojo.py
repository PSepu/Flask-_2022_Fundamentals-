<<<<<<< HEAD
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/encuesta') 
def landing():
    return render_template("Encuesta.html")

@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    ciudad = request.form['ciudad']
    lenguaje = request.form['lenguaje']
    return render_template('show.html', first_name=nombre, last_name=apellido, ciudad = ciudad, lenguaje =lenguaje)

if __name__=="__main__":    
=======
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/encuesta') 
def landing():
    return render_template("Encuesta.html")

@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    ciudad = request.form['ciudad']
    lenguaje = request.form['lenguaje']
    return render_template('show.html', first_name=nombre, last_name=apellido, ciudad = ciudad, lenguaje =lenguaje)

if __name__=="__main__":    
>>>>>>> a1c6ab4e4e7f7a752ce78a63e8ebc0edb11348d7
    app.run(debug=True)