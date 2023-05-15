from flask import Flask, render_template, request, session, redirect
import json
import plotly
import plotly.graph_objects as go
import pandas as pd

app = Flask(__name__)
app.secret_key = 'CLAVE_SECRETA'

dataFrame = pd.read_json('http://127.0.0.1:5000',convert_dates=True)
longitudes = []
latitudes = []
nivelEstacion = []

#Se ingresa las coordenadas a las listas que se usaran en el mapa
for i in range(len(dataFrame)):
    longitudes.append(dataFrame['longitud'][i])
    latitudes.append(dataFrame['latitud'][i])
    nivelEstacion.append(dataFrame['nivel'][i])
    


def generarMapa():
    map = go.Figure(go.Densitymapbox(lat=latitudes,lon=longitudes,z=nivelEstacion,radius=20, opacity= 0.9, zmin=0, zmax=100))
    map.update_layout(mapbox_style="stamen-terrain",mapbox_center_lon=-75.581096,mapbox_center_lat=6.2429)
    map.update_layout(margin={"r": 0,"t": 0,"l": 0, "b": 0})
    mapaJson = json.dumps(map, cls=plotly.utils.PlotlyJSONEncoder)   
    return render_template('mapa.html',mapa=mapaJson)

@app.route('/')
def index():
    if 'username' in session:  # Verificar si el usuario ya inició sesión
        return generarMapa()
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        #Se traen los usuarios y contraseñas desde el servidor de contraseñas
        users = pd.read_json('http://127.0.0.1:5001',convert_dates=True)
       
        #Se recorren todos los usuarios buscando una coincidencia
        for i in range(len(users)):
            # Verificar si el nombre de usuario y contraseña son correctos
            if username == users['user'][i] and password == users['password'][i]:
                session['username'] = username  # Guardar el nombre de usuario en la sesión
                return redirect('/')  # Redirigir a la página principal después del inicio de sesión

        # Si las credenciales son incorrectas, mostrar un mensaje de error
        error_message = 'Nombre de usuario o contraseña incorrectos'
        return render_template('login.html', error_message=error_message)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar el nombre de usuario de la sesión
    return redirect('/login')  # Redirigir a la página principal después del cierre de sesión

if __name__ == '__main__':
    app.run(port=80,host="0.0.0.0")

