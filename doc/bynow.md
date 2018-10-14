## Implementado

__Cita__:
  Hasta el momento una implementación muy pobre, haciendo de la clase una especie de `struct` con la fecha.
  
__Calendario__: 
   Por ahora con ayuda de la biblioteca `calendar` podemos generar un calendario __HTML__ de un mes y año concreto
   y mostrarlo.
     +__Set Calendario__: Para poder cambiar el mes o año de visualización del calendario.(se le puede pasar
      solo el mes, o el mes y el año, el año por defecto es el 2018)      
      
__Login__:
   He implementado un pequeño login usando como base de datos `redis` y metiendo los valores directamente `admin:admin`
   Tras el login se pasa a la pagina donde podemos ver el calendario.
  
## Tests

  Por ahora los tests implementados son muy básicos y comprueban que los objetos estan creados correctamente con `unittest`.
