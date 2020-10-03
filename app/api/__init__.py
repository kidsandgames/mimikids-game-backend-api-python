from flask import Blueprint

api = Blueprint('api', __name__)

from . import guess  # noqa: E402
