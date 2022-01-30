from flask import Flask, render_template
app = Flask(__name__)

@app.route('/lists')
def render_lists():
    student_info = [
        {'num':1, 'first_name' : 'Michael', 'last_name' : 'Choi','age' : 35},
        {'num':2, 'first_name' : 'John','last_name' : 'Supsupin', 'age' : 30 },
        {'num':3, 'first_name' : 'Mark','last_name' : 'Guillen', 'age' : 25},
        {'num':4, 'first_name' : 'KB','last_name' : 'Tonel', 'age' : 27},
        {'num':5, 'first_name' : 'Magdalena','last_name' : 'Rolando', 'age' : 32},
    ]
    return render_template("TablaHtml.html", students = student_info)

if __name__=="__main__":
    app.run(debug=True) 