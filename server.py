from flask import Flask

app = Flask(__name__)

from routes.route import *

if __name__ =="__main__":
    host = "0.0.0.0" #se cambia la localhost
    port = "80"
    app.run(host, port) #este es un metodo de flask para correr un server