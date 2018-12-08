#Instalación Docker

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
~~~	

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/docker/DOCdocker1.PNG)

~~~
$ sudo docker run hello-world
	*Descarga una imágen de prueba y la ejecuta*	
~~~

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/docker/DOCdocker2.PNG)
