# Despliegue IaaS con Azure
Utilizando Vagrant como orquestador de la máquina virtual, Ansible como script de provisionamiento y Fabric para la automaticación de despliegue y ejecución.

## Provisionamiento con Ansible
Antes de empezar a crear los recursos vamos a ver qué va a necesitar nuestro sistema, ya que utilizaremos esta configuración en la propia creación de nuestra máquina virtual (como configuración inicial para empezar a trabajar en ella con el entorno adecuado).
Por ejemplo, mi aplicación va a necesitar que python 3 este instalado en la máquina, en mi caso, y por sencillez a la hora de instalar los requerimientos de mi aplicación, voy a utilizar pip (pip3), por lo que tendré que tenerlo instalado y posteriormente instalaré, como he dicho, los requerimientos. Para saber los requerimientos de una forma dinámica (podrían cambiar con el tiempo) necesitaremos intalar git para poder descargar el proyecto entero de Github y así además nos aseguramos de tener la última versión. Todo esto se ve reflejado en mi playbook.yml o libro de jugadas que es el archivo que Ansible utilizará para llevar a cabo su trabajo (orden ansible-playbook que se introduce en el Vagrantfile posteriormente) además de decirle que coja todos los archivos hosts que sirven para tener entornos de variables diferentes dependiendo lo que le indiquemos, que permitamos la utilización de sudo pues es necesario para la instalación y que el usuario remoto es widowert(yo).
*Es necesaria la instalación de Ansible en la máquina host.*
[Documentación de Ansible](https://docs.ansible.com/)

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/playbook.PNG)

Este playbook tiene sus fallos, no se debe usar sudo directamente en la versión actual de Ansible en su caso hay que utilizar become además utilizo command en todas las acciones cuando hay funciones especificas para apt y pip. Aquí el playbook actualizado:

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/playbookNEW.PNG)

## Creación de máquina virtual con IaaS. Azure y Vagrant.
Primero necesitamos generar AAD (Azure Active Directory) que es como un entorno delimitado dentro de las capacidades de nuestra subscripción de Azure en el cual podemos delegar permisos a Vagrant para la gestión de algunos recursos. Para esto debemos seguir los siguientes pasos ([Fuente original](https://github.com/Azure/vagrant-azure)):
+ Instalar el CLI de Azure, que es una linea de comando para poder comunicarse y gestionar Azure desde la consola de nuestro sistema. [Cómo instalarlo](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).

+ En tu consola, ejecuta `az login` para entrar en tu cuenta de Azure.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/azure-0.png)

+ Ejecuta `az ad sp create-for-rbac` para crear un ADD con acceso al gestor de recursos de Azure. Se ejecutará con la subscripción que tengas activa.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/azure-1.PNG)

+ Para posterior uso necesitas guardar los valores del tenant, appID, password e id de tu subscripción.

+ Nos descargamos la 'box' de Vagrant para Azure con `vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure`

+ Instalamos los plugin de Vagrant para Azure con `vagrant plugin install vagrant-azure`

+ Ahora es el momento de crear un Vagrantfile (necesitamos tener [instalado Vagrant](https://www.vagrantup.com/docs/installation/) en nuestra máquina host). Para ello nos vamos al directorio de nuestro proyecto y creamos el archivo (este archivo variará dependiendo del tipo de máquina virtual que queramos montar, en nuestro caso es Linux-Ubuntu Server, no está definida porque es la que se utiliza por defecto). En el Vagrantfile definimos que vamos a utilizar Azure y definimos diferentes valores, unos para el uso de clave ssh y su localización, otros para el acceso a los recursos (variables con los valores guardados anteriormente) y otros para modificar los valores por defecto de nuestra máquina virtual a crear como es el nombre, la localización (servidor a usar), puerto de salida,etc.

**Decir que este Vagrantfile tiene explicado en sus comentarios todos sus elementos y decir también de cara a la evalución de la asignatura (y para que no se considere plagio) que parte de este Vagrantfile esta copiado directamente de la [documentación](https://github.com/Azure/vagrant-azure) pero he tratado de comprenderlo en su completitud y lo he conseguido gracias a la documentación y la ayuda del profesor, aunque no he tenido tiempo de "jugar" con él para hacerlo más original.**

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/vagrantfileNEW.PNG)

Para que este Vagrantfile funcione correctamente necesitamos exportar todas las variables que encontramos en él, estas variables son los valores que guardamos anteriormente con la siguiente correspondencia: azure_tenant_id=tenant, client_id=appID, client_secret=password, subscription_id=id de la subscripción que aparece al hacer login en Azure.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/azure-exports.png)

Además, como avisé antes, incluimos el provisionamiento con Ansible para su ejecución justo tras la creación de la máquina.

+ Una vez tenemos el Vagrantfile y todo lo necesario instalado ejecutamos `sudo -E vagrant up --provider=azure` para levantar nuestra máquina. En mi caso tengo que usar sudo y para mantener las variables definidas en este entorno tengo que usar la opción -E.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/vagrantup1.PNG)

Resultados de Ansible tras la creación de la máquina.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/vagrantup2.PNG)

Para comprobar que todo va bien podemos conectarnos por ssh con `vagrant ssh` estando en la carpeta del proyecto y, una vez conectados, ejecutamos la aplicación, que la podemos encontrar en /vagrant ya que lanzamos la máquina desde esta carpeta y es compartida, o en el directorio principal que es donde hicimos el git clone con el provisionamiento y es donde se encontrará nuestra aplicación realmente.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/vagrantssh1.PNG)

Nuestra máquina podemos gestiornarla desde el portal de Azure.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/azure-portal-mv.PNG)

Además de todos los recursos relacionados con ella y que se crearon con ella.

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/azure-portal-recursos.PNG)

# Despliegue y ejecución con Fabric
Ya tenemos nuestra aplicación en una máquina virtual con todo lo que necesita para funcionar correctamente, ahora necesitamos poder comunicarnos de una forma eficaz y sencilla con esta maquina para llevar a cabo acciones como Encender, Apagar, Actualizar nuestra aplicación o instalar algún nuevo módulo para una nueva versión, etc.([Operaciones Fabric](http://docs.fabfile.org/en/1.14/api/core/operations.html)) Para esto usamos Fabric, que mediante funciones de Python y diferentes utilidades podemos definir diferentes acciones a llevar a cabo dependiendo de la función principal que llamemos. (Necesitamos instalar Fabric en la máquina host como programa para lanzar las acciones y como biblioteca para crear el fabfile e importar las funciones)

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/fabfileNEW.PNG)

Se ejecuta el archivo con la acción necesaria con la orden `fab -f <localización del fabfile.py> -H <usuario@host tipo ssh> "Accion"`, por ejemplo, yo llevo a cabo el inicio de mi aplicación con `fab -f despliegue/fabfile.py -H vagrant@proyectoiv.westeurope.cloudapp.azure.com "Start"`

![img](https://raw.githubusercontent.com/widowert/ProyectoIV/master/doc/img/azure/azure-fab.PNG)

