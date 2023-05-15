from flask import Flask, request, jsonify
import pandas as pd


api = Flask(__name__)

estaciones = []
json = pd.read_json('http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/?format=json',convert_dates=True)

for station in json['datos']:
    estaciones.append({
        "nivel": round(station['porcentajeNivel'],3),
        "longitud": round(station['coordenadas'][0]['longitud'],4),
        "latitud": round(station['coordenadas'][0]['latitud'],4)
    })

@api.route('/')
def obtenerEstaciones():
    return estaciones

if __name__ == '__main__':
    api.run(host='0.0.0.0',port=5000)