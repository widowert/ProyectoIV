
#  DOCKER

En esta documentación explicaré varias cosas relacionadas con el *docker* creado para este proyecto:

* Como instalar, configurar y crear un docker a partir de una aplicación.
* Como compartir este docker vía DockerHub y enlazarlo con GitHub para su automatización.
* Como desplegarlo con Heroku y, de nuevo, automatizar el despliegue enlazando con GitHub.

La finalidad del *docker* es poder aislar la ejecución de una aplicación en un *contenedor* de forma que este contenga todo lo necesario para su correcto funcionamiento, sin generar ni entrar en conflicto con cualquier versión que haya en el sistema ya que al correr dentro del *contenedor* corre en su propia abstracción del sistema, la cual incluye los datos ( requerimientos incluidos ) y estado necesarios en el que se encontrara la aplicación antes de "empaquetarla" en el *docker*.

# Creación del docker

## Pre instalación:

Para proceder a la instalación, primero, debemos asegurarnos de no tener otras versiones:
~~~
$ sudo apt-get remove docker docker-engine docker.io
~~~
Actualizamos nuestros repos y paquetes:
~~~
$ sudo apt-get update
$ sudo apt-get upgrade
~~~
Instalamos los paquetes necesarios de Docker:
~~~
$ sudo apt-get install \
  apt-transport-https \
  ca-certificates \
  curl \
  software-properties-common
~~~
Importamos la clave GPG oficial de Docker:
~~~
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
~~~
Verificamos la huella con los 8 últimos caracteres ( huella digital oficial= 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C __0EBF CD88__ ):
~~~
$ sudo apt-key fingerprint 0EBFCD88
~~~
Añadimos el repositorio al sistema:
~~~
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
~~~
Actualizamos los cambios:
~~~
$ sudo apt-get update
~~~

## Instalación:

Instalamos docker-ce:
~~~
$ sudo apt-get install docker-ce
~~~
Verificamos que está correctamente instalado y funcionando:
~~~
$ systemctl status docker.service
	*Debe de estar activo*
$ sudo docker run hello-world
	*Descarga una imágen de prueba y la ejecuta*
~~~

## Creación de Docker:
