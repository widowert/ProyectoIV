# Microservicio de gestión de citas
[![Build Status](https://travis-ci.org/widowert/ProyectoIV.svg?branch=master)](https://travis-ci.org/widowert/ProyectoIV)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://proyectoiv.herokuapp.com)

## Proyecto

__Gestor de citas:__
Mediante un login nos meteremos en nuestra cuenta, nos aparecera un calendario personalizado dependiendo de nuestras
citas, del profesional elegido, dias libres, etc. Aqui además podremos elegir fecha y hora para cierto profesional y que esta cita quede registrada en nuestra cuenta y en el sistema para otros que quieran cita con el mismo profesional.__(EN DESARROLLO)__

Voy a desarrollar este microservicio ya que podría servir de apoyo para el desarrollo de una página web de una empresa familiar, además, se pretende su máxima integracion en cualquier aplicación.

## Documentación:

[__Descripción del proyecto__](https://widowert.github.io/ProyectoIV/doc/description)

[__Progreso, hecho hasta ahora__](https://widowert.github.io/ProyectoIV/doc/bynow)

[__Configuración Heroku__](https://widowert.github.io/ProyectoIV/doc/heroku)

[__Docker__](https://widowert.github.io/ProyectoIV/doc/docker)


## PaaS Elegido: Heroku

He elegido Heroku por su simplicidad y porque tras varios intentos con otros PaaS ha demostrado ser el más amigable; además de ser gratuito para servicios básicos como los que necesito para este proyecto. 

**despliegue** : [proyectoiv](https://proyectoiv.herokuapp.com)

## Docker

Para el uso de docker en este proyecto lo he subido para que cualquiera pueda usarlo en DockerHub y además lo tengo desplegado en Heroku.

Contenedor: https://dockerproyectoiv.herokuapp.com/

Repositorio en DockerHub: https://hub.docker.com/r/widowert/proyectoiv/


## Herramientas:

+ Lenguaje: `python`.
+ Framework: `flask`
+ Tests: `unittest` _, y_ `Travis CI` _para su integracion con Github_
+ PaaS: `HEROKU`


