## Implementado

__Citas__:
    Única clase hasta el momento, donde se encuentran todos los métodos necesarios para
    la correcta lectura e interpretación de los json (en /data) donde están guardadas
    las citas libres (dia y hora libre) y otro json donde están guardadas las citas que
    se han registrado (dia y hora de la cita + usuario que la ha cogido).
    Los métodos hasta ahora solo permiten consultar 
    el status de la aplicación junto con ejemplos de uso (página principal), 
    las citas libres para un dia concreto,
    todas las citas libres para cualquier dia, 
    las citas ocupadas de un usuario concreto y 
    todas las citas ocupadas por cualquier usuario y en cualquier dia.
    Además, he añadido nuevas funcionalidades para que se puedan modificar los json a modo de base de datos (tanto añadir nuevas citas ya       sean libres u ocupadas, como eliminar cualquiera de ellas.)
    
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://proyectoiv.herokuapp.com)
  
## Tests

  Por ahora los tests implementados comprueban que los objetos estan creados correctamente y que los valores devueltos (citas) por los métodos de la clase son correctos (lo esperado) si le pasamos parámetros de citas que no existen o que si existen (en modo testing). Además, comprueban en comparación con la aplicación desplegada en Heroku, que los datos de los json son correctos y que se pueden tanto añadir como eliminar citas correctamente (estos tests necesitan de una futura modificación, pues fallarán si no están los datos sincronizados, los de Heroku y Github, de forma que si en Heroku elimino una cita, en Github no y el test podría fallar.)

[![Build Status](https://travis-ci.org/widowert/ProyectoIV.svg?branch=master)](https://travis-ci.org/widowert/ProyectoIV)
