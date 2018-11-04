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
    todas las citas ocupadas por cualquier usuario.
    
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://proyectoiv.herokuapp.com)
  
## Tests

  Por ahora los tests implementados  comprueban que los objetos estan creados correctamente,los valores devueltos (citas) si le pasamos parámetros de citas
  que no existen o que si existen en todos los métodos de la única clase Citas.

[![Build Status](https://travis-ci.org/widowert/ProyectoIV.svg?branch=master)](https://travis-ci.org/widowert/ProyectoIV)