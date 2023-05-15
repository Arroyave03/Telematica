from flask import Flask, request, jsonify

app = Flask(__name__)

Usuarios = [{'user': 'admin', 'password': 'admin'},
            {'user': 'usuario', 'password': '1234'},
            {'user': 'usuario2', 'password': '5678'}
            ]

@app.route('/')
def obtenerUsuarios():
    return Usuarios

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001) #Start Flask using the configuration of config.yml