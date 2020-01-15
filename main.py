from api.v1 import sensors
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(sensors.blueprint)
    app.run()
