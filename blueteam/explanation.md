Sistema de Detección de Intrusiones

Requisitos: 
- python3
- Scapy
- ufw o iptables 

Pasos del script
- Configura un archivo de registro (ids_alerts.log) de logs.
- Se inicia la escucha del trafico TCP/IP, este no se detiene
- Por cada paquete capturado se revisa su info
- Busca el puerto 6200, una conextion en este puerto despues de la sesion FTP indica que el backdoor se ha activado y la maquina esta comprometida
- Una vez detectado el ataque al puerto 6200, se usa el comando 'sudo ufw deny 21/tcp' para bloqeuar el puerto.


