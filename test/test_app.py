import pytest, json, requests
import os
from requests import *

url = 'https://proyectoiv.herokuapp.com/'
with open('data/occupiedDates.json', 'r') as f:
	citasOcupadas = json.load(f)
with open('data/freeDates.json') as f:
	citasLibres=json.load(f)

def test_root():
	response = requests.get(url)
	assert response.status_code==200, "Respuesta incorrecta"
	assert response.json()['status'].upper() == "OK", "No existe status ok"

def test_getDates():
	response = requests.get(url+'getDates/'+citasOcupadas[0]['username'])
	assert response.json()[0]['username'] == citasOcupadas[0]['username'], "No se obtiene información del usuario"
	assert response.json()[0]['date'] == citasOcupadas[0]['date'], "No se obtiene información del usuario"
	assert response.json()[0]['hour'] == citasOcupadas[0]['hour'], "No se obtiene información del usuario"

def test_getAllOccupiedDates():
	response = requests.get(url+'getAllOccupiedDates')
	assert len(response.json()) == len(citasOcupadas), "No se muestran todas las citas"

def test_getAllFreeDates():
	response = requests.get(url+'getAllFreeDates')
	assert len(response.json()) == len(citasLibres['dates']), "No se muestran todas las citas"

def test_getFreeDates():
	response = requests.get(url+'getFreeDates/'+citasLibres['dates'][0]['date'])
	assert response.json()[0] == citasLibres['dates'][0], "No encuentra la fecha"
	response = requests.get(url+'getFreeDates/11/11/18')
	#hay 3 horas para el mismo día
	assert len(response.json()) == 3, "No ha encontrado todas las citas"
