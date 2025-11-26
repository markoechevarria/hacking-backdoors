La vulnerabilidad en vsftpd 2.3.4 es una puerta trasera (backdoor) que permite la ejecución de comandos de forma remota (RCE).


- Paso Clave: La vulnerabilidad se activa enviando el carácter :) como parte del nombre de usuario durante el inicio de sesión.

- Payload: El exploit abre una puerta trasera en el puerto 6200.


Pasos:

1. Sistema victima debe tener Debian o Ubuntu Server (el ubuntu pesa bastante :v) ya que esas maquinas presentan la vulnerabilidad vsftpd 2.3.4

2. Se instala en una vm (para esta demostracion) 
3. Se configura la VM con el modo bridge Adapter (basicamente se simula un entorno real en el que esta conectado a un red) y obitene una direccion IP
4. Se obtiene la IP publica del router (en la vida real), esto no se vera para este proyecto, pero basicamente seria usar tecnicas de hacking para obtener la ip publica de la maquina victima en la vida real.
5. Se ejecuta el script con la ip de la maquina victima
- Se conecta al puerto FTP (21) de la victima
- Se activa el backdoor enviando el comando USER ftpd:) con una contarsena (PASS password), el ataque se activa con el :) .
- Esto activa el servicio vsfftpd y abre el backdoor en el puerto 6200
- El script se desconecta del puerto 21 y se conecta al 6200 
- El script provee de una shell para poder ejecutar comandos en la maqina victima

Con esto habremos ganado acceso a la maquina victima con permisos del servicio FTP, despues vendrian tecnicas de escalada de privilegios pero no se tocara en este proyecto.
