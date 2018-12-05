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
    #dates=Citas()
    #dates.addFreeDate()
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

@app.route('/deleteFreeDate/<int:dia>/<int:mes>/<int:anio>/<string:hour>', methods=['DELETE'])
def deleteFreeDate(dia,mes,anio,hour):
    dates=Citas()
    return dates.deleteFreeDate(str(dia)+"/"+str(mes)+"/"+str(anio),hour)

@app.route('/addFreeDate/<int:dia>/<int:mes>/<int:anio>/<string:hour>', methods=['POST'])
def addFreeDate(dia,mes,anio,hour):
    dates=Citas()
    return dates.addFreeDate(str(dia)+"/"+str(mes)+"/"+str(anio),hour)

@app.route('/deleteOccupiedDate/<int:dia>/<int:mes>/<int:anio>/<string:hour>', methods=['DELETE'])
#remember to create deleteOccupiedDate by username and other route to that new method
def deleteOccupiedDate(dia,mes,anio,hour):
    dates=Citas()
    return dates.deleteOccupiedDate(str(dia)+"/"+str(mes)+"/"+str(anio),hour)

@app.route('/addOccupiedDate/<int:dia>/<int:mes>/<int:anio>/<string:hour>/<string:username>', methods=['POST'])
#remember to create deleteOccupiedDate by username and other route to that new method
def addOccupiedDate(dia,mes,anio,hour,username):
    dates=Citas()
    return dates.addOccupiedDate(str(dia)+"/"+str(mes)+"/"+str(anio),hour,username)

@app.route("/add/<string:dateType>/<int:dia>/<int:mes>/<int:anio>/<string:hour>/<string:username>",  methods=['POST'])
@app.route("/add/<string:dateType>/<int:dia>/<int:mes>/<int:anio>/<string:hour>",  methods=['POST'])
def addOneDate(dateType,dia,mes,anio,hour,username=None):
    if dateType == "free":
        dates=Citas()
        return dates.addFreeDate(str(dia)+"/"+str(mes)+"/"+str(anio),hour)
    elif dateType == "occupied":
        if username != None:
            dates=Citas()
            return dates.addOccupiedDate(str(dia)+"/"+str(mes)+"/"+str(anio),hour,username)
        else:
            return jsonify({"ERROR":"Para añadir una cita tipo occupied se necesita un usuario valido"})
    else:
        return jsonify({"ERROR":"El tipo de cita a añadir solo puede ser free o occupied"})


@app.route("/delete/<string:dateType>/<int:dia>/<int:mes>/<int:anio>/<string:hour>",  methods=['DELETE'])
def deleteOneDate(dateType,dia,mes,anio,hour):
    if dateType == "free":
        dates=Citas()
        return dates.deleteFreeDate(str(dia)+"/"+str(mes)+"/"+str(anio),hour)
    elif dateType == "occupied":
            dates=Citas()
            return dates.deleteOccupiedDate(str(dia)+"/"+str(mes)+"/"+str(anio),hour)
    else:
        return jsonify({"ERROR":"El tipo de cita a añadir solo puede ser free o occupied"})


@app.errorhandler(404)
def error404(e):
    return jsonify({'ERROR':"Page not found",
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
