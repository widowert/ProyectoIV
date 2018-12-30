# Microservicio de gestión de citas
[![Build Status](https://travis-ci.org/widowert/ProyectoIV.svg?branch=master)](https://travis-ci.org/widowert/ProyectoIV)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://proyectoiv.herokuapp.com)

## Proyecto

__Gestor de citas:__
Esta aplicación es una base para un gestor completo de citas. Su funcionalidad está reducida a almacenar tanto las citas libres como ocupadas en json's. Estas citas cuentan con métodos para ser consultadas, modificadas, añadidas o eliminadas. Todas las interacciones con la aplicación se llevan a cabo vía html (de cara al usuario) y las respuestas se dan en json cumpliendo modelo RESTful.

Voy a desarrollar este microservicio ya que podría servir de apoyo para el desarrollo de una página web de una empresa familiar, además, se pretende su máxima integracion en cualquier aplicación.

__Uso:__
+ __Consultar__ (GET): 
  - /getFreeDates/10[dia]/11[mes]/18[año] devuelve un JSON con las horas libres ese día.
  - /getDates/username devuelve un JSON con tus citas si las hay, las citas de username.
  - /getAllFreeDates devuelve un JSON con todas las citas libres registradas.
  - /getAllOcuppiedDates devuelve JSON con todas las citas ocupadas.
  - /status para el estado de la aplicación
+ __Añadir__ (POST):
  - /addFreeDate/dia/mes/año/hora o /add/free/dia/mes/año/hora para registrar (añadir) una nueva cita libre
  - /addOccupiedDate/dia/mes/año/hora/username o /add/occupied/dia/mes/año/hora/username para registrar una nueva cita ocupada
+ __Eliminar__ (DELETE):
  - /deleteFreeDate/dia/mes/año/hora o /delete/free/dia/mes/año/hora para eliminar una cita libre registrada
  - /deleteOccupiedDate/dia/mes/año/hora o /delete/occupied/dia/mes/año/hora para eliminar una cita ocupada
  
## Documentación:

[__Descripción del proyecto__](https://widowert.github.io/ProyectoIV/doc/description)

[__Progreso, hecho hasta ahora__](https://widowert.github.io/ProyectoIV/doc/bynow)

[__Configuración Heroku__](https://widowert.github.io/ProyectoIV/doc/heroku)

[__Docker__](https://widowert.github.io/ProyectoIV/doc/docker)

[__IaaS Azure,Vagrant,Ansible y Fabric__](https://widowert.github.io/ProyectoIV/doc/azure)


## PaaS Elegido: Heroku

He elegido Heroku por su simplicidad y porque tras varios intentos con otros PaaS ha demostrado ser el más amigable; además de ser gradtuito para servicios básicos como los que necesito para este proyecto. 

**despliegue** : [proyectoiv](https://proyectoiv.herokuapp.com)

## Docker

Para el uso de docker en este proyecto lo he subido para que cualquiera pueda usarlo en DockerHub y además lo tengo desplegado en Heroku.

Contenedor: https://dockerproyectoiv.herokuapp.com/

Repositorio en DockerHub: https://hub.docker.com/r/widowert/proyectoiv/

## Despliegue IaaS con Azure

Utilizando Vagrant como orquestador de máquina virtual, Ansible como script de provisionamiento y Fabric para la automaticación de despliegue y ejecución.

Despliegue final: proyectoiv.westeurope.cloudapp.azure.com

## Herramientas:

+ Lenguaje: `python`.
+ Framework: `flask`
+ Tests: `unittest` _, y_ `Travis CI` _para su integracion con Github_
+ PaaS: `HEROKU`
+ IaaS : `Azure`
+ Contenedor: `Docker`
+ Provisionamiento : `Amsible`
+ Despliegue: `Fabric`
+ Orquestador MV: `Vagrant`



