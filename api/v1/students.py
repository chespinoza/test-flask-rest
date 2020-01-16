from http import HTTPStatus
from typing import List

from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from .auth import login_required

students: List[object] = []


class StudentsService(Resource):

    method_decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()

    def get(self, student_id=None):
        if not student_id:
            return students
        elif student_id >= 1 and student_id <= len(students):
            return students[student_id - 1]
        else:
            return make_response(jsonify("Student not found"), HTTPStatus.NOT_FOUND)

    def post(self,):
        self.reqparse.add_argument(
            "name", type=str, required=True, help="Name required for the student"
        )
        self.reqparse.add_argument(
            "age", type=int, required=True, help="Age required for the student"
        )
        args = self.reqparse.parse_args()
        students.append({"name": args["name"], "age": args["age"]})

    def delete(self, student_id):
        if student_id >= 1 and student_id <= len(students):
            del students[student_id - 1]
        else:
            return make_response(jsonify("Student not found"), HTTPStatus.NOT_FOUND)
