from flask import Flask
from os import environ


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<H1>Hello, World!</H1>',200
@app.route('/opcional')
def opcional():
    return '<H1>Hola, Mundo, Opcional!</H1>',200
if __name__ == '__main__':
    app.run("0.0.0.0", int(environ.get('PORT', 8080)))
    
