from flask import Blueprint
from flask.views import View, MethodView


app_api = Blueprint('app_api', __name__)

from . import views_api