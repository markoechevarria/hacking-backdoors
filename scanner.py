import nmap
import sys

def escanear_puertos(host):
    nm = nmap.PortScanner()    
    argumentos = '-p 1-10000 -T4 -v' # -T4
    print(f"[*] Iniciando escaneo de puertos en: {host}")
    
    try:
        nm.scan(host, arguments=argumentos)
        
        if host not in nm.all_hosts():
            print("[!] El host no está disponible o no respondió al escaneo.")
            return
        print("-" * 40)
        
        for proto in nm[host].all_protocols():
            print(f"Protocolo : {proto.upper()}")
            
            lport = nm[host][proto].keys()
            
            sorted_ports = sorted(lport)
            
            for port in sorted_ports:
                state = nm[host][proto][port]['state']
                name = nm[host][proto][port]['name']
                print(f"Puerto: {port}\tEstado: {state}\tServicio: {name}")

        print("-" * 40)

    except nmap.PortScannerError as e:
        print(f"[!] Error de Nmap: {e}")
    except Exception as e:
        print(f"[!] Ocurrió un error inesperado: {e}")
    print("Escaneo terminado")

if __name__ == "__main__":
    target_ip = '127.0.0.1' 
    if len(sys.argv) > 1:
        target_ip = sys.argv[1]
        
    escanear_puertos(target_ip)
