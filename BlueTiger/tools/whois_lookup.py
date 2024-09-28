import subprocess
from colorama import Fore

def whois_lookup(domain):
    print(Fore.CYAN + f"\n*** WHOIS Lookup pour {domain} ***\n")
    try:
        result = subprocess.run(['whois', domain], capture_output=True, text=True)
        print(Fore.GREEN + result.stdout)
    except FileNotFoundError:
        print(Fore.RED + "La commande 'whois' n'est pas disponible sur votre système.")
    except Exception as e:
        print(Fore.RED + f"Erreur inattendue: {e}")
