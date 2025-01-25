from flask import (Blueprint, g, render_template)

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def register():
    return "ciao"