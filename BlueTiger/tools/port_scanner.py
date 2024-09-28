import socket
from colorama import Fore

def scan_ports(target_ip):
    print(Fore.CYAN + f"\n*** Scanning ports for {target_ip} ***\n")
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(Fore.GREEN + f"Port {port}: Ouvert")
        sock.close()
    print(Fore.CYAN + f"\nFin du scan pour {target_ip}")
