from random import random

from flask import Blueprint, jsonify

blueprint = Blueprint("sensors", __name__, url_prefix="/api/v1/sensors")


@blueprint.route("/data", methods=("GET", "POST"))
def sensors_list():
    return jsonify(label=int(10 * random()), score=random())
