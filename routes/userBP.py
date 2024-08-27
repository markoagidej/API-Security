from flask import Blueprint
from controllers.userController import save, getAll

user_blueprint = Blueprint('user_bp', __name__)
user_blueprint.route('/', methods=['POST'])(save)
user_blueprint.route('/', methods=['GET'])(getAll)