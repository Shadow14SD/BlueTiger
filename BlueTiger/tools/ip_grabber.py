import requests
from colorama import Fore

def grab_ip_info(ip_address=None):
    try:
        print(Fore.CYAN + "\n*** IP Grabber Tool ***\n")
        
        if ip_address is None:
            response = requests.get('https://ipinfo.io')
            print(Fore.YELLOW + "Aucune IP spécifiée, récupération de votre IP publique...\n")
        else:
            response = requests.get(f'https://ipinfo.io/{ip_address}')
            print(Fore.YELLOW + f"Récupération des informations pour l'IP {ip_address}...\n")
        
        if response.status_code == 200:
            data = response.json()
            print(Fore.GREEN + f"IP: {Fore.WHITE}{data.get('ip', 'Inconnue')}")
            print(Fore.GREEN + f"Ville: {Fore.WHITE}{data.get('city', 'Inconnue')}")
            print(Fore.GREEN + f"Région: {Fore.WHITE}{data.get('region', 'Inconnue')}")
            print(Fore.GREEN + f"Pays: {Fore.WHITE}{data.get('country', 'Inconnu')}")
            print(Fore.GREEN + f"Fournisseur (Org): {Fore.WHITE}{data.get('org', 'Inconnu')}")
            print(Fore.GREEN + f"Localisation: {Fore.WHITE}{data.get('loc', 'Inconnue')}\n")
        else:
            print(Fore.RED + f"Erreur: Impossible de récupérer les informations IP (Code HTTP: {response.status_code})")
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Erreur de connexion : {e}")
    except Exception as e:
        print(Fore.RED + f"Erreur inattendue : {e}")
