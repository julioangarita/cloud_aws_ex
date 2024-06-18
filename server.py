from flask import Flask

app = Flask(__name__)

from routes.route import *

if __name__ =="__main__":
    host = "127.0.0.1"
    port = "8080"
    app.run(host, port) #este es un metodo de flask para correr un server