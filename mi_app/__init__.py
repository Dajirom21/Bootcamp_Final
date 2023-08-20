from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('base_de_datos.db')
cursor = conn.cursor()


cursor.execute('SELECT * FROM usuarios')
resultados = cursor.fetchall()


tabla_html = '<table>'
for fila in resultados:
    tabla_html += '<tr>'
    for columna in fila:
        tabla_html += f'<td>{columna}</td>'
    tabla_html += '</tr>'
tabla_html += '</table>'


conn.close()


print(tabla_html)



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/purchase")
def purchase():
    return render_template("purchase.html")

@app.route("/status")
def status():
    return render_template("status.html")



