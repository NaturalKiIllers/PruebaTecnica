# PruebaTecnica
¡Hola! 
Para poder ejecutar la aplicación debe realizar los siguientes pasos:
-	Clone y/o el repositorio PruebaTecnica
-	Una vez descargados habrá la carpeta backend en su visualizador favorito e introduzca el siguiente comando “docker-compose up” esto lo que hará es crear un contenedor y que a su vez cargue todas las dependencias presentes en “requirements.txt” una vez lo haya activado y cargado todas las dependencias, el back estaría listo para su utilización y prueba.
o	El Back cuenta con las siguientes url: 
   *  http://127.0.0.1:8000/users/ Este se encarga de listar todos los usuarios cargados en la base de datos 
   *  http://127.0.0.1:8000/contexts/ Este se encarga de listar todos los contexts cargados en la base de datos
   * http://127.0.0.1:8000/events/ Se encarga de cargar todos los eventos cargados.
   * Finalmente, el más importante es http://127.0.0.1:8000/userl/? Que es el que listara todos los eventos de acuerdo con los filtros indicados. Y el cual se conecta directamente con el frontend.
   * En caso de que quiera ver todos los eventos de un usuario en especifico seria de la siguiente manera http://127.0.0.1:8000/userl/?username=ingresar_username  
   * Y así sucesivamente con todos los filtros, usted puede realizar la consulta por un solo filtro como por varios a la vez.
-	Para el caso del Frontend es exactamente lo mismo, una vez se descomprime, se ingresa a su visualizador y escribe el mismo comando que en el back “docker-compose up”, este se encargara de preparar el entorno para la ejecución del sistema web, su url seria: http://localhost:3000/
-	Una vez dentro de la página web al inicio no mostrara nada más que los campos y el botón de filtrado, usted puede ingresar username, evento_type, evento_source, fecha y hora, una vez ingresado los campos que desee filtrar aprete el botón que realiza la consulta a la base de datos y retorna una tabla filtrada.
 *  Puede utilizar de ejemplo los siguientes valores, pero si necesita más datos puede ocupar el backend para ver toda la lista de usuarios. f98e6b50b0a6b9c57cb2eea7f7cb43ce713244ee4df3fc2d175a06ef76f88b8e
  * Para el caso de event_type puede ingresar estos valores: 	-edxucursos-callback
  * Para el caso de event_source puede ingresar estos valores: Server
  *	Para el caso de course_id puede ingresar estos valores: course-v1:eol+FOR-GEO+2023_1
  * 	Para el caso de fecha puede ingresar estos valores: 2023-04-02
  *	Para el caso de hora puede ingresar estos valores: 23:00

-	Una vez finalizada o quiera cambiar los campos debe hacer un F5 o recargar la página para que se limpien los campos y la tabla.
-	Importante aclarar los campos mostrados son la key que esa es el número de sesión que se vincula con la mayoría de los campos que relaciona eventos, usuarios y contexto.
-	Finalmente, si no quiere seguir trabajando en el back y front presione ctrl+c para detener los entornos.
