from flask import Flask, render_template
app = Flask(__name__)    
#
#@app.route('/dojo')          
#def print_dojo():
#    return 'Dojo!' 

#@app.route('/say/<name>')  
#def hello(name):
#    print(name)
#    return "Hello, " + name

#@app.route('/play') 
#def square():
#    return render_template("AreaJuegos.html",cuadrado=".square")

#@app.route('/play/<veces>') 
#def square_times(veces):
#    return render_template("AreaJuegos.html" ,cantidad=int(veces))

@app.route('/play/<color>/<veces>') 
def square_times_color(color,veces):

    return render_template("AreaJuegos.html",cuadrado=color,cantidad=int(veces))

if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración
