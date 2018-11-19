# coding=utf-8
import os,sys,json
from flask import Flask, render_template, request, redirect, url_for, jsonify

sys.path.append("src/")
from classes import Citas

app = Flask(__name__)
app.config['DEBUG'] = True
#app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = 'super secret key'

@app.route('/')
def index():
    '''myjson = jsonify(
    {"status":"OK",
    "ejemplo de consulta general":{"ruta":"/getFreeDates/10[dia]/11[mes]/18[año]",
                    "return":"{JSON con horas libres ese dia}"
                    }
    ,
    "ejemplo de consulta propia":{"ruta":"/getDates/username",
                    "return":"{JSON con tus citas si las hay}"
    },
    "consultar todas las citas libres":{"ruta":"/getAllFreeDates",
                    "return":"{JSON con todas las citas libres}"
    },
    "cnsultar todas las citas registradas":{"ruta":"/getAllOcuppiedDates",
                    "return":"{JSON con todas las citas registradas}"
    }
    })
    response = app.response_class(
        response = myjson,
        status = 200,
        mimetype = 'application/json'
    )'''
    return jsonify({
    "status":"OK",
    "ejemplo de consulta general":{"ruta":"/getFreeDates/10[dia]/11[mes]/18[año]",
                    "return":"{JSON con horas libres ese dia}"
                    }
    ,
    "ejemplo de consulta propia":{"ruta":"/getDates/username",
                    "return":"{JSON con tus citas si las hay}"
    },
    "consultar todas las citas libres":{"ruta":"/getAllFreeDates",
                    "return":"{JSON con todas las citas libres}"
    },
    "consultar todas las citas registradas":{"ruta":"/getAllOcuppiedDates",
                    "return":"{JSON con todas las citas registradas}"
    }
    })
    #return redirect(url_for('status'))
@app.route('/status')
def status():
    return jsonify({"status":"OK"})


@app.route('/getFreeDates/<int:dia>/<int:mes>/<int:anio>')
@app.route('/getFreeDates/<int:dia>/<int:mes>')
def getFreeDates(dia=None,mes=None,anio=18):
    '''freeDates=[]
    searchDate=str(dia)+"/"+str(mes)+"/"+str(anio)
    if os.path.exists('data/freeDates.json'):
        with open('data/freeDates.json','r') as file:
            fD=json.load(file)
            for date in fD['dates']:
                if date['date'] == searchDate:
                    freeDates.append(date)
    else:raise IOError("Cant find freeDates.json")
    if freeDates == []:
        return jsonify({'Error':"Dates not found",
        'Message':"No se han encontrado citas libres para la fecha  "+ searchDate})
    else:
        return jsonify(freeDates)'''
    dates=Citas()
    return dates.getFreeDates(dia,mes,anio)

@app.route('/getAllFreeDates')
def getAllFreeDates():
    dates=Citas()
    return dates.getAllFreeDates()

@app.route('/getAllOccupiedDates')
def getAllOccupiedDates():
    dates=Citas()
    return dates.getAllOccupiedDates()

@app.route('/getDates/<string:username>')
def getDates(username=None):
    dates=Citas()
    return dates.getMyDates(username)

@app.errorhandler(404)
def error404(e):
    return jsonify({'ERROR':"Page not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
