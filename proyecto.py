# coding=utf-8
import os
import datetime #datetime para controlar la fecha actual
import calendar #calendar para la creacion de calendarios HTML
import json
from pymongo import MongoClient #import redis #database
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'super secret key'

client = MongoClient()
db = client.proyecto
'''
proyect = db.proyecto
proyect.insert({
    'username' : "oscar",
    'password' : "oscar"
})
proyect.insert({
    'username' : "admin",
    'password' : "admin"
})'''

"""class Usuario:

    def authentication(self,name,password):
        r = redis.Redis()
        login = str(r.get(name+":"+password))
        if login == "None":
            return False
        else:
            return True"""

class Cita:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
class Calendario:
    #Clase del calendario, que será entorno a lo que gire todo
    #posteriormente
    def __init__(self):
        self.dOcuped=[]

    def setCalendario(self,month,year):
        cl=calendar.HTMLCalendar()
        calendario=cl.formatmonth(year,month)
        with open("./templates/calendario.html","w") as html:
            html.write(calendario)
            html.close()

    def generaCalendarioHoyHTML(self):
        x=datetime.datetime.now()
        cl=calendar.HTMLCalendar()
        calendario=cl.formatmonth(x.year,x.month)
        with open("./templates/calendario.html","w") as html:
            html.write(calendario)
            html.close()

    def aniadirCita(self,cita):
        self.dOcuped.append(str(cita.day)+"/"+str(cita.month)+"/"+str(cita.year))
        print(self.dOcuped)
        print(str(cita.day)+"/"+str(cita.month)+"/"+str(cita.year))

    def getOcuped(self):
        return self.dOcuped

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/calendar')
def calendario():
    return render_template('calendario.html')

def authentication(name,password):
    '''r = redis.Redis()
    login = str(r.get(name))
    if login != password:
        return False
    else:
        r.set(name,True)
        return True'''
    proyect = db.proyecto
    existing_user = proyect.find_one({'username' : name})
    if existing_user is not None:
        if existing_user['password'] == password:
            return True
    return False

def alreadyConnected(name):
    '''r = redis.Redis()
    return r.get(name)'''
    proyect = db.proyecto
    existing_user = proyect.find_one({'username' : name})
    if existing_user is not None:
        return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        """if request.form['username']=='admin':
            if authentication(request.form['username'],request.form['password']):
                return render_template('admin.html')
        else:"""
        if authentication(request.form['username'],request.form['password']): #or alreadyConnected(request.form['username']):
            #return redirect(url_for('calendario'))
            return jsonify({'Identification' : {'status' : "OK",'username' : request.form['username']}})
        else:
            return render_template('login.html')
    return render_template('login2.html')

"""@app.route('/uid')
def uid():
    return request.sid()"""

@app.route('/addingdate')
def addNewDate():
    cita = Cita(request.args.get('day',type=int,default=0),request.args.get('month',type=int,default=0),request.args.get('year',type=int,default=0))
    calendario.aniadirCita(cita)
    return "Cita añadida correctamente"
@app.route('/setcalendario')
def setCalendario():
    calendario.setCalendario(request.args.get('month',type=int,default=1),request.args.get('year',type=int,default=2018))
    return redirect(url_for('index'))
@app.errorhandler(404)
def error404(e):
    return '<html><head>ERROR 404</head><body><p>ERROR 404</p></body></html>',404

if __name__ == '__main__':

    """calendario = Calendario()
    cita=Cita(01,02,2000)
    calendario.aniadirCita(cita)
    print calendario.getOcuped()"""
    '''r = redis.Redis()
    r.set("oscar","oscar")
    r.set("admin","admin")'''
    calendario = Calendario()
    calendario.generaCalendarioHoyHTML()
    app.run(host='0.0.0.0', debug=True)
    #app.run(host='0.0.0.0', debug=True, port='8080')
