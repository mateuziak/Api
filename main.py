import csv
from flask import Flask, jsonify

app = Flask('flaskconftest')

@app.route('/api/funcionarios')       
def root():
    with open('funcionarios.csv', newline='') as file:
        reader = csv.DictReader(file)
        funcionarios = [row for row in reader]
    return jsonify(funcionarios)

@app.route('/api/cargos') 
def root2():
    with open('cargos.csv', newline='') as file:
        reader = csv.DictReader(file)
        cargos = [row for row in reader]
    return jsonify(cargos)

app.run()
