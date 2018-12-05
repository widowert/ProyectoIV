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

def test_deleteAndAddDates():
	response = requests.get(url+'getAllOccupiedDates')
	tamOccup = len(response.json())

	response = requests.get(url+'getAllFreeDates')
	tamFree = len(response.json())


	requests.delete(url+'delete/occupied/11/11/18/13:00')
	response = requests.get(url+'getAllOccupiedDates')

	assert len(response.json()) == tamOccup-1, "No se elimina correctamente la cita occupied"
	requests.post(url+'add/occupied/11/11/18/13:00/oscar')
	response = requests.get(url+'getAllOccupiedDates')
	assert  len(response.json()) == tamOccup, "No se aniade correctamente la cita occupied"


	requests.delete(url+'delete/free/11/11/18/18:00')
	response = requests.get(url+'getAllFreeDates')

	assert len(response.json()) == tamFree-1, "No se elimina correctamente la cita free"
	requests.post(url+'add/free/11/11/18/18:00')
	response = requests.get(url+'getAllFreeDates')
	assert len(response.json()) == tamFree, "No se aniade correctamente la cita free"
