from flask_restful import Resource, reqparse


class Hello(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

    def get(self):
        return {"msg": "Hello"}

    def post(self):
        self.reqparse.add_argument(
            "name", type=str, required=True, help="Name required for the greeting"
        )
        args = self.reqparse.parse_args()
        return {"Hello": args["name"]}
