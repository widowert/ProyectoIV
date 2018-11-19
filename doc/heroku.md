# HEROKU

## Inicio:

Para empezar tenemos que haber **completado el servicio web en GitHub**. De forma que cuando lo despleguemos pueda ser correctamente desplegado sin errores.
Nos metemos en la [página principal](https://www.heroku.com/ "Heroku main page") de **Heroku** y **nos registramos**.

## Instalación:
Una vez registrados, logeados y teniendo github a punto para desplegar procedemos a crear la aplicación (el método que voy a describir es el más sencillo y es solo para desplegar un servicio, pero no hago nada localmente, todo desde Heroku.

Dentro de nuestra **área personal** nos vamos a la parte derecha y clickamos en **New -> Create new app**

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/newApp.PNG)



**Elegimos el nombre de nuestra app** (es el que aparecerá en el url de acceso al despliegue) **y la región** donde lo queremos desplegar (por cercanía, para un mejor tiempo de respuesta elegimos Europa)

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/herokuappNameAndRegion.PNG)



Una vez creada lo primero que vamos a hacer es irnos a la pestaña **Deploy** (dentro de nuestra app en la pagina de Heroku)

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/herokuDeploystart.PNG)



Aquí, **elegimos GitHub en Deployement method** y lo enlazamos con nuestra cuenta. Luego **en App connected elegimos el repositorio** donde esta nuestra app **y la rama para deployment**.
En este punto ya tenemos nuestra app conectada, pero como quiero que los cambios que vaya haciendo en Git se actualicen también en mi app tengo que **activar el Automatic Deployment**, este lo **unimos con** el proceso de **Travis (wait for CI to pass)**, para que el deploy automático se haga cuando hagamos cambios y estos hayan pasado los tests definidos para la app.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/herokuDeployoptionsChoosen.PNG)



También podemos quedarnos en el paso de conectar nuestra cuenta y repositorio de GitHub y hacer cada **Deploy manualmente** cuando queramos ver los cambios en la app.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/herokuManualDeploy.PNG)



Tras este proceso ya solo nos queda una cosa, Heroku tiene nuestra app, junto a los requeriments (requeriments.txt) necesarios para ejecutarla, pero **Heroku tiene diferentes tipos de ejecución**, de hecho podemos definir nosotros como queremos que se ejecute. En este caso vamos a querer un proceso de tipo WEB ya que nuestra app es un microservicio web al que quiero acceder por el navegador como usuario. Para 'decirle' esto a heroku tenemos que **definir un Procfile**, donde especificaremos:
`web: gunicorn app:app` donde web es el tipo de proceso que estamos definiendo, dos puntos y la orden explicita que vamos a ejecutar, en este caso, gunicorn (es una interfaz compatible con el framework flask, que es el que uso), el primer app es el nombre de la aplicación (del ejecutable, en mi caso app .py) y especificamos que esa es la app.

Además, tenemos que **especificar(añadir) en los requirements gunicorn**, porque si no heroku no lo importara y al llegar a la ejecución no podrá por no encontrar gunicorn.
