from api.v1 import greetings, sensors, students
from flask import Flask
from flask_restful import Api

app = Flask(__name__)

if __name__ == "__main__":
    # legacy endpoints
    app.register_blueprint(sensors.blueprint)
    # new endpoints
    api = Api(app)
    api.add_resource(greetings.Hello, "/")
    api.add_resource(
        students.StudentsService,
        "/api/v1/students",
        "/api/v1/students/<int:student_id>",
    )

    app.run()
