# Microservicio de gestión de citas

[![Build Status](https://travis-ci.org/widowert/ProyectoIV.svg?branch=master)](https://travis-ci.org/widowert/ProyectoIV)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://proyectoiv.herokuapp.com)

## Proyecto

__Gestor de citas:__
Microservicio orientado a aportar facilidades de cara al sistema interno de citas de cualquier compañia. El microserivcio desarrollado es muy simple pero esboza correctamente la idea. Su funcionalidad no es más que alamacenar citas (tanto libres como ocupadas) y poder consultarlas (todas las libres, todas las ocupadas, por usuario, por fecha) y modificarlas (por ahora la modificación es eliminar y añadir).

Voy a desarrollar este microservicio ya que podría servir de apoyo para el desarrollo de una página web de una empresa familiar, además, se pretende su máxima integracion en cualquier aplicación.

## Documentación:

[__Descripción del proyecto__](https://widowert.github.io/ProyectoIV/doc/description)

[__Progreso, hecho hasta ahora__](https://widowert.github.io/ProyectoIV/doc/bynow)

[__Despliegue Heroku__](https://widowert.github.io/ProyectoIV/doc/heroku)

## PaaS Elegido: Heroku

He elegido Heroku por su simplicidad y porque tras varios intentos con otros PaaS ha demostrado ser el más amigable; además de ser gratuito para servicios básicos como los que necesito para este proyecto. 

## Herramientas
+ Lenguaje: `python`.
+ Framework: `flask`
+ Tests: `unittest` _, y_ `Travis CI` _para su integracion con Github_
+ PaaS: `HEROKU`

## Instalación de dependecias
pip install -r requirements.txt

## Uso de la aplicacion
_Ejecución app_ `python app.py` (version python testeada 3.6.6)
En la raíz / redirige a /status donde puedes ver el status y ejemplos de uso.

_Ejecución tests_ `pytest` (version python testeada 3.6.6)
