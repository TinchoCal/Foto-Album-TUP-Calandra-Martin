from flask import Flask
from photo_album.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from photo_album.routes import *  

if __name__ == '__main__':
    app.run(debug=True)  