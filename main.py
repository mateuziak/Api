import csv
from flask import Flask, jsonify

app = Flask('flaskconftest')

@app.route('/api/dados')       
def root():
    with open('dados.csv', newline='') as file:
        reader = csv.DictReader(file)
        dados = [row for row in reader]
    return jsonify(dados)
app.run()