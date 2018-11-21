
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

Primero tenemos que crear un **dockerfile**, este contendrá la información necesaria para que docker pueda formar nuestro contenedor "personalizado" para ello tenemos que especificar, entre otras cosas, el lenguaje y versión de este utilizada ( he de añadir que para un mismo lenguaje hay versiones de imágenes más o menos pesadas, habiendo probado algunas más livianas me decidí por mantener la mía, bastante pesada, por haber tenido problemas con las demás ), las ordenes necesarias para arrancar el docker e instalar las dependencias de nuestra app y la orden necesaria para ejecutar la propia app así como el puerto donde correrá.

DOC3

Una vez tenemos el dockerfile terminado y en la carpeta de nuestro proyecto, podemos **construir el docker** ( no necesario si queremos utilizar *DockerHub*, saltar al siguiente paso si fuera el caso ):
~~~
$ sudo docker build -t proyectoiv
~~~
Podemos comprobar que está creado consultando las imágenes de nuestro sistema:
~~~
$ sudo docker images
~~~
Lo ejecutamos en nuestro sistema (localmente) especificando el puerto donde estará en el docker nuestra app y al puerto que queremos redirigirlo además del nombre puesto anteriormente (tuve problemas con esto, ya que uso vagrant y hay más de una redirección de puerto, puede que no sea necesaria esta opción *-p*):
~~~
$ sudo docker run -p 80:80 -it proyectoiv
~~~

# DockerHub

En este punto, tenemos nuestro docker listo, ahora nuestro interés en DockerHub no es más que compartirlo, de forma que cualquiera mediante una sola orden en la consola pueda descargarselo y correrlo en su sistema. También señalar que el docker creado anteriormente esta montado a partir de nuestro proyecto en GitHub y como DockerHub permite su sincronización con GitHub, una vez subido los cambios a nuestro repo( dockerfile ) DockerHub se encarga de montárnoslo automáticamente, por lo que el anterior podríamos decir que fue para probarlo localmente.

Para empezar vamos a [DockerHub](https://hub.docker.com/) y nos creamos una cuenta.

DOC4

Una vez creada nos vamos a los ajustes de nuestra cuenta, al apartado de cuentas y servicios enlazados.

DOC5

Una vez enlazado, podemos crear un docker a partir de nuestro repo y además cada cambio que hagamos, se guardara automáticamente en nuestro docker de DockerHub.

DOC6

DOC7

DOC8

y listo, tenemos nuestro docker creado, compartido (descarga y ejecución en una orden) y automatizado (cambios en GitHub generan build automática).

# Despliegue Heroku
