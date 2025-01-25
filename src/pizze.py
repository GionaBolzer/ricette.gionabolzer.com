from flask import (Blueprint, g, render_template, request)
from datetime import datetime,timedelta

bp = Blueprint('pizze', __name__, url_prefix='/pizze')

@bp.route('/pizzaCapuano', methods=['GET'])
def register():
    # numero pizze e ora di cena
    
    n_pizze = request.args.get('pizze',1) 
    ora_cena = request.args.get('ora',"19:30")
    
    if n_pizze == "":
        n_pizze = int(1)
    if int(n_pizze) <= 0:
        return "404"
    else:
        n_pizze =int(n_pizze)
    if ora_cena == "":
        ora_cena = "19:30"

    ora_cena_obj = datetime.strptime(ora_cena, '%H:%M')

    titolo = "Pizza Napoletana Contemporanea con biga ad alta idratazione di Vincenzo Capuano"
    video = "https://www.youtube.com/watch?v=L7z9u_RKQFk"
    
    # BIGA
    farina_biga = round(500/6*n_pizze,0)
    acqua_biga = round(250/6*n_pizze,0)
    lievito_biga = round(5/6*n_pizze,2)
    ora_biga_frigo = (ora_cena_obj + timedelta(hours=1.5)).strftime('%H:%M')
    
    # Autolisi
    farina_autolisi = round(500/6*n_pizze,0)
    acqua_autolisi = round(250/6*n_pizze,0)
    ora_autolisi = (ora_cena_obj + timedelta(hours=19)).strftime('%H:%M')

    # Chiusura
    acqua_chiusura = round(300/6*n_pizze,0)
    lievito_chiusura = round(1/6*n_pizze,2)
    sale_chiusura = round(25/6*n_pizze,0)
    ora_chiusura = (ora_cena_obj + timedelta(hours=19,minutes=30)).strftime('%H:%M')

    

    return render_template('pizze/pizzaCapuano.html',
                           titolo=titolo,
                           video=video,
                           n_pizze=n_pizze,
                           ora_cena=ora_cena,
                           farina_biga=farina_biga,
                           acqua_biga=acqua_biga,
                           lievito_biga=lievito_biga,
                           ora_biga_frigo=ora_biga_frigo,
                           farina_autolisi=farina_autolisi,
                           acqua_autolisi=acqua_autolisi,
                           ora_autolisi=ora_autolisi,
                           acqua_chiusura=acqua_chiusura,
                           lievito_chiusura=lievito_chiusura,
                           sale_chiusura=sale_chiusura,
                           ora_chiusura=ora_chiusura
                        )