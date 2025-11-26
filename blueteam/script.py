from scapy.all import sniff, TCP
import logging
import os
import time

PORT_TO_CLOSE = 21
LOG_FILE = "ids_alerts.log"
ATTACK_SIGNATURES = [
    (6200, "vsftpd_backdoor_RCE") 
]
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def cerrar_puerto(port):
    print(f"\n[!!! ALERTA DE RESPUESTA !!!] Bloqueando puerto {port} en el firewall...")
    logging.warning(f"Respuesta Automática: Bloqueando puerto {port}.")
    
    try:
        os.system(f"sudo ufw deny {port}/tcp")
        print(f"[+] Puerto {port} bloqueado correctamente. Verifique el estado de ufw.")
    except Exception as e:
        print(f"[!] Error al intentar cerrar el puerto: {e}. ¿Tienes permisos de sudo?")


def analizar_paquete(paquete):
    """Analiza cada paquete en busca de actividad sospechosa."""
    if TCP in paquete:
        ip_origen = paquete['IP'].src
        ip_destino = paquete['IP'].dst
        dport = paquete['TCP'].dport
        sport = paquete['TCP'].sport
        
        if dport == 6200:
            alerta_msg = f"POSIBLE EXPLOTACIÓN: Tráfico inusual detectado en el puerto 6200 (vsftpd Backdoor). Origen: {ip_origen}"
            print(f"\n[ALERTA ROJA] {alerta_msg}")
            logging.critical(alerta_msg)
            
            cerrar_puerto(PORT_TO_CLOSE)
            return True 

def iniciar_ids():
    print(f"[*] IDS Iniciado. Escuchando tráfico. Registros en: {LOG_FILE}")
    print(f"[*] Puerto de respuesta automática: {PORT_TO_CLOSE}")
    
    sniff(prn=analizar_paquete, stop_filter=analizar_paquete, store=0)

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[!] Advertencia: Ejecuta este script con 'sudo' para capturar tráfico y cerrar puertos.")
        print("    Ejemplo: sudo python3 ids_script.py")
    else:
        iniciar_ids()
