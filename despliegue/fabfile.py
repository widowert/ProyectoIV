#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import *
import urllib

def Delete():
	#Borrar la carpeta del proyecto actual
	sudo('rm -rf ProyectoIV')
	print("Deleted ProyectoIV succesfully")
def Install():
	with cd('ProyectoIV'):
		#Instalar los requirements del proyecto
		run('pip3 install -r requirements.txt')
		print("Instaled new requirements succesfully")
def CheckTests():
	#Para comprobar los tests de Travis accedo a la imágen que Travis da como Status de mi proyecto
	request=urllib.urlopen('https://api.travis-ci.org/widowert/ProyectoIV.svg?branch=master')
	content=request.read()
	#si en esta imágen aparece la palabra passing pasa los tests, si no pondría failling u otra cosa
	if str(content).find("passing") != -1:
		return True
	else:
		return False
def Update():
	if CheckTests():
		#Borramos el proyecto anterios para actualizarlo con Git
		Delete()
		#Nos bajamos el proyecto en su version actual de Git(estable)
		#con los tests ya pasados en Travis, no necesitamos hacerlo aqui
		run('git clone https://github.com/widowert/ProyectoIV.git')
		#Reinstalamos los requirements por si algo hubiera cambiado
		Install()
		print("Updated project succesfully!!")
	else:
		print("The current version on Github is not stable, not passing tests, not updated but stable")
def Start():
	with cd('ProyectoIV'):
		print("Started succesfully, your app is in the air!\n")
		print("Remember to stop it if you want or it will keep flying")
		#Ejecución de la aplicación con gunicorn y guardamos pid en gunicorn.pid
		sudo('gunicorn app:app --bind 0.0.0.0:80 --pid gunicorn.pid')

def catpid(): #comando de pruebas para ir viendo si guarda pid
	with cd('ProyectoIV'):
		run('cat gunicorn.pid')

def ClassicStart():
	with cd('ProyectoIV'):
		print("Flask started succesfully, remember its going to stop when you leave")
		#Ejecución de la aplicación con python, se para al salir
		#por lo que no necesitamos funcion de Stop
		sudo('python3 app.py')

def Stop():
	#Matamos el proceso de gunicorn para parar la ejecucion
	#sudo('pkill gunicorn')
	sudo('kill -9 `cat ProyectoIV/gunicorn.pid`') #matamos solo al proceso gunicorn que controla nuestra app (por si hubiera otros)
	print("Stoped succesfully, your app is down")
def UpdateSystem():
	sudo('apt-get update')
	print("Everything up to date")
	sudo('apt-get upgrade')
