from flask import Blueprint

api = Blueprint('api', __name__)

from . import guess_things  # noqa: E402
