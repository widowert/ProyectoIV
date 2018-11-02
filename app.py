# coding=utf-8
import os
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = 'super secret key'

@app.route('/')
def index():
    return redirect(url_for('status'))
@app.route('/status')
def status():
    return jsonify({
    "status":"OK",
    "ejemplo de consulta general":{"ruta":"/getFreeDates/10[dia]/11[mes]/18[año]",
                    "return":"{JSON con horas libres ese dia}"
                    }
    })
    ''',
    "ejemplo de consulta propia":{"ruta":"/getFreeDates/username/10[dia]/11[mes]/18[año]",
                    "return":"{JSON con tus citas si las hay}"
    },
    "ejemplo de registro cita":{"ruta":"/takeDate/username/10[dia]/11[mes]/18[año]/1400[hora de comienzo cita sin ':']",
                    "return":"{JSON con la cita escogida y las que tuvieras}"
    }
    })'''
@app.route('/getFreeDates/<int:dia>/<int:mes>/<int:anio>')
@app.route('/getFreeDates/<int:dia>/<int:mes>')
def getFreeDates(dia=None,mes=None,anio=18):
    freeDates=[]
    searchDate=str(dia)+"/"+str(mes)+"/"+str(anio)
    if os.path.exists('data/freeDates.json'):
        with open('data/freeDates.json','r') as file:
            fD=json.load(file)
            for date in fD['dates']:
                if date['date'] == searchDate:
                    freeDates.append(date)
    else:raise IOError("Cant find freeDates.json")
    return jsonify(freeDates)
@app.errorhandler(404)
def error404(e):
    return '<html><head>ERROR 404</head><body><p>ERROR 404</p></body></html>',404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
