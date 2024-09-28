from colorama import Fore, init
from tools.ip_grabber import grab_ip_info
from tools.port_scanner import scan_ports
from tools.whois_lookup import whois_lookup
from tools.dir_bruteforce import brute_force_directories

# Initialiser colorama
init(autoreset=True)

def display_menu():
    print(Fore.CYAN + """
    Bienvenue dans BlueTiger Tools !
    Sélectionnez une option :
    1. Récupérer l'adresse IP publique ou d'une cible
    2. Scanner les ports d'une cible
    3. Requête WHOIS pour un domaine ou une IP
    4. Brute-force des répertoires d'un site web
    5. Quitter
    """)

def main():
    while True:
        display_menu()
        choice = input(Fore.LIGHTBLUE_EX + "Entrez votre choix : ")

        if choice == '1':
            ip_address = input(Fore.LIGHTBLUE_EX + "Entrez une IP (laisser vide pour votre IP publique) : ")
            grab_ip_info(ip_address if ip_address else None)
        elif choice == '2':
            target_ip = input(Fore.LIGHTBLUE_EX + "Entrez l'IP à scanner : ")
            scan_ports(target_ip)
        elif choice == '3':
            domain = input(Fore.LIGHTBLUE_EX + "Entrez le domaine ou l'IP pour la requête WHOIS : ")
            whois_lookup(domain)
        elif choice == '4':
            url = input(Fore.LIGHTBLUE_EX + "Entrez l'URL du site web : ")
            wordlist = input(Fore.LIGHTBLUE_EX + "Entrez le chemin du fichier wordlist : ")
            brute_force_directories(url, wordlist)
        elif choice == '5':
            print(Fore.YELLOW + "Au revoir !")
            break
        else:
            print(Fore.RED + "Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
