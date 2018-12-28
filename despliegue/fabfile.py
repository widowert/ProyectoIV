#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import *

def Delete():
	#Borrar la carpeta del proyecto actual
	run('sudo rm -rf ProyectoIV')
def Install():
	with cd('ProyectoIV'):
		#Instalar los requirements del proyecto
		run('pip3 install -r requirements.txt')
def Update():
	#Borramos el proyecto anterios para actualizarlo con Git
	Delete()
	#Nos bajamos el proyecto en su version actual de Git(estable)
	#con los tests ya pasados en Travis, no necesitamos hacerlo aqui
	run('git clone https://github.com/widowert/ProyectoIV.git')
	#Reinstalamos los requirements por si algo hubiera cambiado
	Install()	
def Start():
	with cd('ProyectoIV'):
		#Ejecución de la aplicación con gunicorn
		run('sudo gunicorn app:app --bind 0.0.0.0:80')
def ClassicStart():
	with cd('ProyectoIV'):
		#Ejecución de la aplicación con python, se para al salir
		#por lo que no necesitamos funcion de Stop
		run('sudo python3 app.py')
def Stop():
	#Matamos el proceso de gunicorn para parar la ejecucion
	run("sudo pkill gunicorn")
