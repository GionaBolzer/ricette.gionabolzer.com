from flask import (Blueprint, g, render_template, request)
from datetime import datetime,timedelta

bp = Blueprint('pizze', __name__, url_prefix='/pizze')


def checkIntParameter(parameters, default):
    if parameters == "":
        parameters = int(default)
    if int(parameters) <= 0:
        return "404"
    else:
        parameters =int(parameters)
    return parameters

    
@bp.route('/pizzaCapuano', methods=['GET'])
def pizzaCapuano():
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


@bp.route('/pizzaCanotto', methods=['GET'])
def pizzaCanotto():
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

    titolo = "Pizza Canotto di Vincenzo Abbate"
    video = "https://www.youtube.com/watch?v=RffhpDygcsg"
    
    # BIGA
    farina_biga = round(1000/6*n_pizze,0)
    acqua_biga = round(500/6*n_pizze,0)
    lievito_biga = round(7/6*n_pizze,2)

    # Chiusura
    acqua_chiusura = round(250/6*n_pizze,0)
    lievito_chiusura = round(4/6*n_pizze,2)
    sale_chiusura = round(30/6*n_pizze,0)
    ora_chiusura = (ora_cena_obj).strftime('%H:%M')

    

    return render_template('pizze/pizzaCanotto.html',
                           titolo=titolo,
                           video=video,
                           n_pizze=n_pizze,
                           ora_cena=ora_cena,
                           farina_biga=farina_biga,
                           acqua_biga=acqua_biga,
                           lievito_biga=lievito_biga,
                           acqua_chiusura=acqua_chiusura,
                           lievito_chiusura=lievito_chiusura,
                           sale_chiusura=sale_chiusura,
                           ora_chiusura=ora_chiusura
                        )
    


@bp.route('/pizzaInTeglia', methods=['GET'])
def pizzaInTeglia():
    # numero pizze e ora di cena
    
    n_pizze = 1
    n_teglie = request.args.get('n_teglie',1) 
    larghezza = request.args.get('larghezza',30) 
    lunghezza = request.args.get('lunghezza',40) 
    ora_cena = request.args.get('ora',"19:30")
    
    n_teglie = checkIntParameter(n_teglie, 1)
    larghezza = checkIntParameter(larghezza, 40)
    lunghezza = checkIntParameter(lunghezza, 30)
    
    if n_teglie == "404" or larghezza == "404" or lunghezza == "404":
        return "404"
    
    if ora_cena == "":
        ora_cena = "19:30"

    ora_cena_obj = datetime.strptime(ora_cena, '%H:%M')

    titolo = "Pizza in teglia ad alta idratazione"
    video = "https://www.youtube.com/watch?v=d7RrRqeiIZY"
    
    peso_panetto = (larghezza*lunghezza)/2
    peso_totale = peso_panetto*n_teglie

    # BIGA
    farina = round(0.555555*peso_totale,0)
    acqua = round(0.444444*peso_totale,0)
    lievito = round(0.003888*peso_totale,2)
    sale = round(0.01388*peso_totale,0)
    print(f"sale= {sale}")
    ora_chiusura = (ora_cena_obj - timedelta(hours=4)).strftime('%H:%M')


    return render_template('pizze/pizzaInTeglia.html',
                           titolo=titolo,
                           video=video,
                           n_teglie=n_teglie,
                           larghezza=larghezza,
                           lunghezza=lunghezza,
                           ora_cena=ora_cena,
                           farina=farina,
                           acqua=acqua,
                           lievito=lievito,
                           sale=sale,
                           peso_panetto=peso_panetto,
                           ora_chiusura=ora_chiusura
                        )