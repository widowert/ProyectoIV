#COPIADO DE LA DOCUMENTACION - INICIO - FUENTE:https://github.com/Azure/vagrant-azure

Vagrant.configure('2') do |config| #Establecemos la versión de Vagrant a utilizar (puede ser 1 o 2) que influye en la configuración por defecto
  #en la version 1 no podríamos utilizar por ejemplo config.vm.provider, aunque ambas versiones se pueden combinar en un mismo vagrantfile pero en bloques diferentes

  config.vm.box = 'azure' # se especifica la "box" a utilizar  (estableze el entorno de Vagrant espcifico para la función que queramos darle a la maquina)
  #la caja que utilicemos tiene que estar instalada en nuestro vagrant local, en nuestro caso es una caja "dummy" o caja falsa, esta se utiliza para poder
  #en primera instancia usar Vagrant, aunque luego en Azure utilizaremos otra máquina, que, como no la definimos, por defecto es Ubuntu
  #esta caja se llama azure porque nosotros le hemos puesto ese nombre al instalarla en vagrant (ver docu) pero le podriamos dar cualquier nombre

  config.ssh.private_key_path = '~/.ssh/id_rsa' #definimos la ruta de nuestras llaves ssh a utilizar, por defecto en los sistemas Ubuntu se almacenan aqui,
  #aunque si quisieramos utilizar otras llaves en otra localizacion solo tendríamos que especificarlo aqui

  config.vm.provider :azure do |azure| #definimos que nuestro proveedor será azure para que vagrant use la configuracion especifica para este proveedor
  # ademas generamos una variable llamada azure (podriamos llamarla de cualquier manera) para poder añadir configuración o información complementaria y necesaria
  # aunque estos datos de configuracion que vamos a definir a continuación por defecto se buscarían en el mismo sitio que le indicamos (variables de entorno)

    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

#COPIADO DE LA DOCUMENTACION - FINAL

# los siguientes datos de configuración por defecto serían diferentes, al definirlos podemos "personalizar" nuestra maquina

    azure.vm_name = "proyectoiv" #definimos el nombre a utilizar para nuestra maquina, se ve reflejado en la ruta de acceso y en la propia maquina

    azure.vm_size = 'Basic_A0' #definimos el tamaño a utilizar, esto es importante en otros casos, ya que con este tamaño definimos la memoria disponible
    #para ejecutar aplicaciones y cargas de trabajo (además de consideraciones para la implementacion de la maquina), en la generacion actual hay tamaños especificos para diferentes usos de CPU, diferentes tráficos de red,etc
    # dependiendo del uso que vayamos a hacer de la maquina, en nuestro caso usamos el MÁS básico de todos y de la generacion anterior, el cual es extra pequeño
    # perfecto para lo que necesitamos (prueba básica), para más info ver https://docs.microsoft.com/es-es/azure/virtual-machines/linux/sizes-previous-gen#basic-a

    azure.tcp_endpoints = "80" #definimos el tcp endpoint para poder acceder desde el navegador, el cual utiliza el puerto 80, si no lo definimos no podremos acceder, solo por ssh
    #aunque tambien podemos cambiarlo y añadirlo desde azure manualmente

    azure.location = "westeurope" #definimos la localización del servidor donde se alhojara nuestra maquina, esto es importante pues por defecto es en el oeste de estados unidos y el retardo de
    #conexion es considerable, teniendo en cuenta que estamos en europa

    azure.admin_username = "widowert"

  end

  config.vm.provision :ansible do |ansible| #definimos la forma de provision (podriamos hacerla directamete aqui meidante el provisionador :shell que es la shell de vagrant), en nuestro caso especificamos que utilizaremos
  #ansible y declaramos una variable (ansible, es una variable, podemos usar cualquier nombre) para poder especificarle el archivo (playbook) a utilizar

      ansible.playbook = "provision/playbook.yml" #definimos la ruta de nuestro playbook para que sepa donde encontrarlo, decir que podriamos usar el mismo proyecto en diferentes sistemas
      #por lo que podriamos tener diferentes playbooks especificos y aqui se especificariamos (en cada vagrantfile el necesario)

      #En este apartado lo ideal sería copiar mi proyecto (solo los archivos necesarios) en vez de descargar el repo entero en la maquina con Ansible (mediante git clone)
      #pero en cualquier caso si quisiera actualziarlo a distancia no sabría como descargar del repo solo lo necesario y, tal y como lo veo, seria una solucion unicamente inicial
      #ya que con el tiempo (en la primera actualizacion) ya descargaria todos los datos innecesarios para el funcionamiento como la documentacion
  end
end
