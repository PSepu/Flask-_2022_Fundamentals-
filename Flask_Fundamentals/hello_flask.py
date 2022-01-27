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

@app.route('/repeat/<word>/<veces>') 
def word_times(word, veces):
    return render_template("wordTimes.html" ,palabra=(word) , cantidad=int(veces))

if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración
