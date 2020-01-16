# Views.py under owners
from flask import Blueprint, render_template
from myproject import db
from myproject.models import Owner


owners_blueprints = Blueprint('owners', __name__, template_folder='templates/owners')

