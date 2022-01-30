from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/tablero/<ancho>/<largo>') 
def tablero(ancho,largo):
    return render_template("TableroDamas.html",cantidad=int(ancho), cantidadL=int(largo))

if __name__=="__main__":    
    app.run(debug=True)