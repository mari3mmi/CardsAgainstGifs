import random
import string
from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__, url_prefix='/api')

UNIQUE_ROOMS = []

@api_bp.route('/room/create', methods=["GET"])
def get_room():
    id = create_unique_room()
    print(id)
    return jsonify({'room':id, 'error': ''})


def create_unique_room():
    global UNIQUE_ROOMS

    while True:
        N = 5
        id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        if id not in UNIQUE_ROOMS:
            UNIQUE_ROOMS.append(id)
            return id
