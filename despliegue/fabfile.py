#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import *

def Delete():
	#Borramos la carpeta del proyecto actual
	run('rm -rf ProyectoIV')

def Install():
	#Instalamos los requirements por si hubieran cambiado
	run('pip3 install -r ProyectoIV/requirements.txt')

def Update():
	Delete()
	#Nos bajamos el proyecto en su version actual de Git
	run('git clone https://github.com/widowert/ProyectoIV.git')
	Install()
	
def Start():
	#Ejecución de la aplicación con gunicorn
	run('cd ProyectoIV/ && sudo gunicorn app:app --bind 0.0.0.0:80')

def Stop():
	#Matamos los procesos asociados a gunicorn
	run("sudo kill $(ps -ef | grep gunicorn | awk '{print $2}')")
