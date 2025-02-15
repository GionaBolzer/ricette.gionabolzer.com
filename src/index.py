from flask import (Blueprint, g, render_template)

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def register():
    pizze = {
        "Pizza Contemporana alta idratazione in planetaria":'pizzaCapuano',
        "Pizza Canotto di Vincenzo Abbate":'pizzaCanotto',
        "Pizza in teglia ad alta idratazione": 'pizzaInTeglia'
    }
    return render_template('index.html',pizze=pizze)